"""Serializer for user model."""

from rest_framework import serializers
from rest_framework import status

from django.contrib.auth import get_user_model

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "uid",
            "name",
            "phone",
            "email",
            "gender",
            "kind",
            "image",
        )
        read_only_fields = ("id", "uid")


class UserDetailSerializer(UserListSerializer):
    class Meta(UserListSerializer.Meta):
        fields = UserListSerializer.Meta.fields + (
            "status",
            "is_staff",
            "created_at",
            "updated_at",
        )
        read_only_fields = UserListSerializer.Meta.read_only_fields + (
            "created_at",
            "updated_at",
        )


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Specify password and confirm_password fields as write_only, meaning they won't be included in responses
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},  # Styling to indicate it's a password field
        trim_whitespace=False,
    )
    confirm_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    # Custom validation for password to check if it matches confirm_password
    def validate_password(self, value):
        password = value
        confirm_password = self.initial_data.get("confirm_password", "")
        if password != confirm_password:
            raise serializers.ValidationError(
                detail="Password and confirm password don't match!!!",  # Error message
                code=status.HTTP_400_BAD_REQUEST,  # HTTP status code
            )

    class Meta:
        model = User  # Specify the model for the serializer
        fields = (
            "name",
            "phone",
            "email",
            "gender",
            "image",
            "password",
            "confirm_password",
        )  # Fields to include in the serialization

    # Custom create method to handle user creation
    def create(self, validated_data):
        validated_data.pop(
            "confirm_password", None
        )  # Remove confirm_password from validated data
        user = User(**validated_data)  # Create a new user instance with validated data
        user.set_password(validated_data.get("password", ""))  # Set user's password
        user.save()  # Save the user to the database
        return user  # Return the created user instance


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "uid",
            "name",
            "phone",
            "email",
            "gender",
            "image",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "uid",
            "created_at",
            "updated_at",
        )
