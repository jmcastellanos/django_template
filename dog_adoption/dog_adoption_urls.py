from django.urls import path

from dog_adoption.views.dogs_views import NotAdoptedDogsViews
from dog_adoption.views.dog_adoption_view import DogAdoptionView
from dog_adoption.views.payment_view import PaymentView

urlpatterns = [
    path(
        "api/dog_adoption/not_adopted_dogs",
        NotAdoptedDogsViews.as_view(),
        name="get_not_adopted_dogs",
    ),

    path(
        "api/dog_adoption/adoption",
        DogAdoptionView.as_view(),
        name="dog_adoption",
    ),

    path(
        "api/dog_adoption/payment",
        PaymentView.as_view(),
        name="payment",
    ),


]
