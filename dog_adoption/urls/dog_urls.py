from django.urls import path

from dog_adoption.views.dog_adoption_view import DogAdoptionView
from dog_adoption.views.dogs_views import NotAdoptedDogsViews

urlpatterns = [
    path(
        "not_adopted_dogs",
        NotAdoptedDogsViews.as_view(),
        name="get_not_adopted_dogs",
    ),

    path(
        "adoption",
        DogAdoptionView.as_view(),
        name="dog_adoption",
    ),

]
