from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from django_template.external_services.paypal_service import PaypalService
from django_template.external_services_provider import ExternalApisProvider
from dog_adoption.models import Adoption, Dog, Person
from dog_adoption.resolvers.create_adoption_resolver import CreateAdoptionResolver
from dog_adoption.serializers import AdoptionSerializer, DogSerializer


class NotAdoptedDogsViews(APIView):

    def get(self, request):
        """
        Retrieves all the dogs that don't have owner yet
        """
        # filtering dogs
        dogs = Dog.objects.filter(adoption__isnull=True)
        # serializing dogs
        data = DogSerializer(instance=dogs, many=True).data

        return Response(data=data)


class DogAdoptionView(APIView):

    def post(self, request, ):
        """
        Creates and adoption using a resolver.
        """
        resolver = CreateAdoptionResolver()
        adoption = resolver.resolve(
            person_id=request.data["person_id"],
            dog_id=request.data["dog_id"],
        )

        return Response(
            data={"adoption_id": str(adoption.id)},
            status=HTTPStatus.CREATED,
        )

    def get(self, request):
        """
        Retrieves all the adoptions
        """
        adoptions = Adoption.objects.all()
        data = AdoptionSerializer(instance=adoptions, many=True,).data
        return Response(data=data)


class PaymentView(APIView):

    def post(self, request, ):
        """
        Creates and adoption
        """
        apis_provider = ExternalApisProvider()
        paypal_api = apis_provider.get_paypal_api()
        paypal_service = PaypalService(paypal_api=paypal_api)
        payment_id = paypal_service.create_payment(
            owner=request.data["owner"],
            source=request.data["source"],
            destination=request.data["destination"],
        )
        return Response(data={"payment_id": payment_id})
