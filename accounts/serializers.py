from foods.serializers import FoodSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField('get_photo_url')
               

    def get_photo_url(self, obj):
        request = self.context.get('request')
        
        if request and obj.photo:
            photo_url = obj.photo.url
            return request.build_absolute_uri(photo_url)
        else:
            return None

    

    class Meta:        
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone', 'first_name', 'last_name','photo_url',  'address', 'date_joined', 'last_login']
     



class DashboardSerializer(serializers.Serializer):

    user = UserSerializer(read_only=True)
    token = serializers.CharField()
    foods = FoodSerializer(many=True, read_only=True)