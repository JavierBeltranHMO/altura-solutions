import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "Bug Fix"},
                    "unit_amount": 5000,  # 50.00 USD
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("payment_success")),
        cancel_url=request.build_absolute_uri(reverse("payment_cancel")),
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
    return render(request, "payments/cancel.html")


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


