from rosevideo.dvdrental.serializers import *
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = AuthGroup.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

class RenewalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows renewals to be viewed or edited.
    """
    queryset = Renewal.objects.all()
    serializer_class = RenewalSerializer
    permission_classes = (permissions.IsAuthenticated,)

class RentalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rentals to be viewed or edited.
    """
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = (permissions.IsAuthenticated,)

class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (permissions.IsAuthenticated,)

class InventoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows inventories to be viewed or edited.
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated,)

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)

class StaffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows staff to be viewed or edited.
    """
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (permissions.IsAuthenticated,)

class StoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stores to be viewed or edited.
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAuthenticated,)

class FilmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows films to be viewed or edited.
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

