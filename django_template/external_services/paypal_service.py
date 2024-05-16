import random
from abc import ABCMeta, abstractmethod


class PaypalInterface(metaclass=ABCMeta):
    """
    Interface for paypal apis
    We will have a fake api and the real one. You can simulate an error api also

    This interface is the one that the service will use. See PaypalService class
    """

    @abstractmethod
    def create_payment(
        self,
        owner: str,
        source: str,
        destination: str,
    ) -> str:
        raise NotImplementedError


class FakeApi(PaypalInterface):
    """
    This would be a fake api. Will always work.
    Used for local and maybe development environments
    """

    def create_payment(
        self,
        owner: str,
        source: str,
        destination: str,
    ) -> str:
        print(f"""Fake paypal:
        owner: {owner}, source:{source}, destination: {destination}""")

        # creating a fake payment id
        numbers = [str(x) for x in range(10)]
        random.shuffle(numbers)
        return "fake_payment_" + "".join(numbers)


class PaypalApi(PaypalInterface):
    """This would be the real api. The one that really makes requests to paypal"""

    def __init__(self):
        # this api could have a particular init implementation with credentials
        pass

    def create_payment(
        self,
        owner: str,
        source: str,
        destination: str,
    ) -> str:
        print(f"""Simulating a request to paypal
        owner: {owner}, source:{source}, destination: {destination}""")
        # here we hit the paypal api, and paypal returns a response
        # simulating we have made a hit a we have an id

        # creating a payment id
        numbers = [str(x) for x in range(10)]
        random.shuffle(numbers)
        return "payment_" + "".join(numbers)


class PaypalService:
    """
    Paypal Service, the one that will be used in our code.
    """

    def __init__(self, paypal_api: PaypalInterface):
        self.__paypal_api = paypal_api

    def create_payment(
        self,
        owner: str,
        source: str,
        destination: str,
    ) -> str:
        return self.__paypal_api.create_payment(
            owner=owner,
            source=source,
            destination=destination,
        )
