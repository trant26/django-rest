from rest_framework import serializers
from gara.models import Car
from django.contrib.auth.models import User

class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Car
        fields = ('id', 'vehicle_name', 'model', 'seria_number', 'year', 'cost', 'amount_sale', 'owner')

class UserSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'car')