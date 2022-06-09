from rest_framework import serializers
from core.models import Faq, User, Block


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('title', 'description')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('user', 'warn', 'permanent')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'user_id_tg', 'warn')

    def create(self, validated_data):
        return User.objects.create(**validated_data)
