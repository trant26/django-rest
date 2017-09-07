from rest_framework import serializers
from gara.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vehicle_name', 'model', 'seria_number', 'cost', 'amount_sale')

# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     vehicle_name = serializers.CharField(max_length=256)
#     model = serializers.CharField(max_length=256)
#     seria_number = serializers.CharField(max_length=256)
#     # year = serializers.DateField()
#     cost = serializers.FloatField()
#     amount_sale = serializers.FloatField()

#     def create(self, validated_data):
#         """
#         Create and return a new 'gara' instance
#         """
#         return Gara.objects.create(**validated_data)

#     def update(self, validated_data):
#         """
#         Update and return an existing 'gara' instance
#         """
#         instance.vehicle_name = validated_data.get('vehicle_name', instance.vehicle_name)
#         instance.model = validated_data.get('model', instance.model)
#         instance.seria_number = validated_data.get('seria_number', instance.seria_number)
#         # instance.year = validated_data.get('year', instance.year)
#         instance.cost = validated_data.get('cost', instance.cost)
#         instance.amount_sale = validated_data.get('amount_sale', instance.amount_sale)
#         instance.save()
#         return instance
