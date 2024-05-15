from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }