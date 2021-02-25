from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #Django does not provide full url hence we used below for full path in the database
    image  = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null= True,required=False)
    class Meta:
        model = Product
        fields = ['name','description','price','stock','is_active','image','category']
