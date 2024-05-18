from django.urls import include, path

urlpatterns = [
    path(
        "api/dog_adoption/",
        # all the urls that we include here will have the prefix: api/dog_adoption/
        include("dog_adoption.urls.dog_urls"),
    ),
    path(
        "api/dog_adoption/payments/",
        # all the urls that we include here will have the
        # prefix: api/dog_adoption/payments/
        include("dog_adoption.urls.payment_urls"),
    ),


]
