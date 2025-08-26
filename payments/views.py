import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse

from wagtail.models import Page

stripe.api_key = settings.STRIPE_SECRET_KEY


SERVICES_PRICES = {
    "bug-fix": 5000,  # 50.00 USD
    "feature-integration": 12000,  # 120.00 USD
    "mvp": 25000,  # 250.00 USD
}


@csrf_exempt
def create_checkout_session(request):
    service_id = request.POST.get("service")
    if service_id not in SERVICES_PRICES:
        return JsonResponse({"error": "Invalid service"}, status=400)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": service_id.replace("-", " ").title()},
                    "unit_amount": SERVICES_PRICES[service_id],
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("payment_success")),
        cancel_url=request.build_absolute_uri(
            reverse("payment_cancel") + f"?service={service_id}"
        ),
    )
    return JsonResponse({"id": session.id})


def payment_page(request):
    return render(
        request,
        "payments/payment.html",
        {"STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY},
    )


def payment_success(request):
    return render(request, "payments/success.html")


def payment_cancel(request):
    service = request.GET.get("service")
    service_page = Page.objects.filter(slug=service).first()
    return render(
        request,
        "payments/cancel.html",
        {"service": service, "service_url": service_page.url if service_page else "/"},
    )


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        print("✅ Payment succeeded:", session)

    return HttpResponse(status=200)
