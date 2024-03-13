from rest_framework import serializers
from rest_framework.validators import ValidationError
from management.models.user import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'user_name', 'password', 'is_manager']

    def validate(self, attrs):
        user_name_exists = User.objects.filter(user_name=attrs["user_name"]).exists()
        if user_name_exists:
            raise ValidationError("Tên đăng nhập đã được sử dụng")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'user_id': representation['user_id'],
            'name': representation['name'],
            'user_name': representation['user_name'],
            'is_manager': representation['is_manager'],
        }
