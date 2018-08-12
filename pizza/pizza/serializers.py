from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post


#class OrderSerializer(serializers.ModelSerializer):
#    
#    class Meta:
#        fields = ('id', 'customer_id', 'customer_name', 'customer_adress', 'created_at', 'updated_at',)
#        model = models.Order

