from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    tg_id = models.BigIntegerField(
        verbose_name="id телеграма",

    )
    username = models.CharField(
        verbose_name='@пользователя',
        max_length=100,
        unique=True
    )

    address = models.CharField(
        verbose_name='адрес',
        null=True,
        blank=True,
    )
    phone = models.CharField(
        verbose_name='номер телефона',
        null=True,
        blank=True,
    )

    cart = models.OneToOneField(
        'mainapp.Cart',
        on_delete=models.CASCADE,
        related_name='user',
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("tg_id",)

    def __str__(self):
        return f"{self.pk} | {self.username=} | {self.tg_id}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

