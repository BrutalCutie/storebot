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
    cart = models.ForeignKey(
        "mainapp.Cart",
        verbose_name="корзина",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user',
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("tg_id",)

    def __str__(self):
        return f"{self.pk} | {self.username=} | {self.tg_id}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
