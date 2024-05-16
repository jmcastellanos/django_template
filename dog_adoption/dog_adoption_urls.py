from django.urls import path

from dog_adoption.views.dogs_views import NotAdoptedDogsViews, DogAdoptionView,\
    PaymentView

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
