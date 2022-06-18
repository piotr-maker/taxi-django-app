from rest_framework import serializers
from .models import Orders, Locations


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'
        read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    order_from = LocationSerializer(required=True)
    order_to = LocationSerializer(required=True)

    class Meta:
        model = Orders
        fields = ['id', 'order_from', 'order_to', 'status', 'cost', 'created_at', 'updated_at']
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        passenger = validated_data.pop('passenger')
        loc = validated_data.pop('order_from')
        loc_from = Locations(longitude=loc['longitude'], latitude=loc['latitude'], altitude=loc['altitude'])
        loc_from.save()

        loc = validated_data.pop('order_to')
        loc_to = Locations(longitude=loc['longitude'], latitude=loc['latitude'], altitude=loc['altitude'])
        loc_to.save()

        status = validated_data.pop('status')
        cost = validated_data.pop('cost')
        order = Orders(passenger=passenger, order_from=loc_from, order_to=loc_to, status=status, cost=cost)
        order.save()
        return order

    def to_representation(self, instance):
        representation = dict()
        representation['id'] = instance.id
        representation['order_from'] = LocationSerializer(instance.order_from).data
        representation['order_to'] = LocationSerializer(instance.order_to).data
        representation['status'] = instance.status
        representation['cost'] = instance.cost
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation
