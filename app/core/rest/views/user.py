"""Views for Users."""

from django.contrib.auth import get_user_model

from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
)

from core.rest.serializers.user import (
    UserListSerializer,
    UserDetailSerializer,
    UserRegistrationSerializer,
    MeSerializer,
)


User = get_user_model()


class UserList(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserListSerializer
    queryset = User().get_all_actives()


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserDetailSerializer
    queryset = User().get_all_actives()


class UserRegistration(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
    queryset = User().get_all_actives()


class MeDetail(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user
