from rosevideo.dvdrental.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('id', 'username', 'email', 'password')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = ('id', 'name')

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('rental_id', 'rental_date', 'inventory', 'customer', 'return_date', 'staff', 'last_update', 'renewal_token')

    def create(self, validated_data):
        token = Token.objects.create(token=uuid.uuid4(), customer=validated_data['customer'])
        return Rental.objects.create(**validated_data, renewal_token=token)

class RenewalSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=1048, write_only=True)
    class Meta:
        model = Renewal
        fields = ('renewal_id', 'rental', 'new_return_date', 'token')

    def create(self, validated_data):
        if Token.check_token(validated_data.pop('token'), validated_data['rental'].customer):
            return Renewal.objects.create(**validated_data)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_id', 'customer', 'staff', 'rental', 'amount', 'payment_date')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('inventory_id', 'film', 'store_id', 'last_update')

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('film_id', 'language', 'title', 'description', 'release_year', 'rental_duration', 'rental_rate', 'length', 'replacement_cost', 'rating', 'special_features', 'last_update')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'store_id', 'first_name', 'last_name', 'email', 'address', 'active', 'create_date', 'last_update')

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('staff_id', 'store', 'first_name', 'last_name', 'email', 'active', 'username', 'password', 'last_update')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('store_id', 'manager_staff', 'address', 'last_update')

