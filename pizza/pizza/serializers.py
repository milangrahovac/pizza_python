from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post


class OrdersSerializer(serializers.ModelSerializer):
   
   class Meta:
       fields = ('id', 'customer_id', 'customer_name', 'customer_address', 'created_at', 'updated_at',)
       model = models.Orders

