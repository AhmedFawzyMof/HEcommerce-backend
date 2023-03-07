from rest_framework import serializers

from .models import *

from product.serializers import ProductSerializer

class MyOrderItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
            "size",
            "color"
        )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "phone2",
            "address",
            "paypal",
            "ispaid",
            "Delivered",
            "items",
            "order_total",
            "order_status",
            "order_status_Ar"
        )

class OrderItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
            "size",
            "color"
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "phone2",
            "address",
            "paypal",
            "items",
            "order_total",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order


class ContactSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Contact
        fields = (
            "user",
            "phone",
            "message",
        )


class FeedBackSerializer(serializers.ModelSerializer):    
    class Meta:
        model = FeedBack
        fields = (
            "user",
            "title",
            "message",
        )



