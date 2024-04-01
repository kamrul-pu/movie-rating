"""Core models for our app."""

from autoslug import AutoSlugField

from django.contrib.auth.base_user import (
    BaseUserManager,
)
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models

from versatileimagefield.fields import VersatileImageField

from common.models import BaseModelWithUID

from core.choices import (
    UserKind,
    UserGender,
)
from core.utils import get_user_media_path_prefix


class UserManager(BaseUserManager):
    """Managers for users."""

    def create_user(self, name, phone, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address.")

        user = self.model(
            name=name,
            phone=phone,
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, phone, email, password):
        """Create a new superuser and return superuser"""

        user = self.create_user(
            name=name,
            phone=phone,
            email=email,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.kind = UserKind.SUPER_ADMIN
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, BaseModelWithUID, PermissionsMixin):
    """Users Model of the System"""

    name = models.CharField(
        max_length=150,
        blank=True,
        db_index=True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
    )
    phone = models.CharField(
        max_length=20,
        db_index=True,
        unique=True,
    )
    slug = AutoSlugField(
        populate_from="name",
        unique=True,
        db_index=True,
    )
    gender = models.CharField(
        max_length=20,
        blank=True,
        choices=UserGender.choices,
        default=UserGender.UNKNOWN,
    )
    image = VersatileImageField(
        "Profile_image",
        upload_to=get_user_media_path_prefix,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    kind = models.CharField(
        max_length=20,
        choices=UserKind.choices,
        default=UserKind.UNDEFINED,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "name",
        "phone",
    )

    class Meta:
        verbose_name = "System User"
        verbose_name_plural = "System Users"
