from rest_framework.response import Response
from rest_framework.views import APIView

from django_template.external_services.paypal_service import PaypalService
from django_template.external_services_provider import ExternalApisProvider


class PaymentView(APIView):

    def post(self, request, ):
        """
        Simulates a payment. In this view we are only putting an example of a good
        way to call an external service using its api and the defined service
        """

        # selecting the correct api according to the environment
        apis_provider = ExternalApisProvider()
        paypal_api = apis_provider.get_paypal_api()

        # initializing the service with the selected api
        paypal_service = PaypalService(paypal_api=paypal_api)

        # calling the service with the provided api
        payment_id = paypal_service.create_payment(
            owner=request.data["owner"],
            source=request.data["source"],
            destination=request.data["destination"],
        )

        return Response(data={"payment_id": payment_id})
