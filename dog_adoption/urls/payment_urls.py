from django.urls import path

from dog_adoption.views.payment_view import PaymentView

urlpatterns = [
    path(
        "payment",
        PaymentView.as_view(),
        name="payment",
    ),
]
