from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        Fields = ['id','user','product_names','total_product','transaction_id','total_amount','created_at','updated_on']
