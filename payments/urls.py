from django.urls import path
from . import views

urlpatterns = [
    path(
        "create-checkout-session/",
        views.create_checkout_session,
        name="create-checkout-session",
    ),
    path("success/", views.payment_success, name="payment_success"),
    path("cancel/", views.payment_cancel, name="payment_cancel"),
    path("webhook/", views.tripe_webhook, name="stripe_webhook"),
]
