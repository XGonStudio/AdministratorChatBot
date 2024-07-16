import base64
from rest_framework import serializers
from .models import User, UserSocials


class UserSocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSocials
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    image_data = serializers.SerializerMethodField()
    socials = UserSocialsSerializer(source='usersocials', read_only=True)

    def get_image_data(self, obj):
        if obj.photo:
            with open(obj.photo.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'location', 'gender', 'phone_number', 'image_data', 'socials']
