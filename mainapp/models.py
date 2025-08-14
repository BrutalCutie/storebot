import os

from django.db import models


class SubCategory(models.Model):
    category = models.ForeignKey(
        'mainapp.Category',
        on_delete=models.CASCADE,
        verbose_name='Категория прикрепления',
        related_name='subcategories',
    )

    name = models.CharField(
        verbose_name="Наименование подкатегории",
        max_length=100,
    )
    help_text = models.TextField(
        verbose_name='Подробности подкатегории',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.pk} | {self.name=} | {self.category.name}"

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Category(models.Model):
    name = models.CharField(
        verbose_name="Наименование категории",
        max_length=100,
    )
    help_text = models.TextField(
        verbose_name='Подробности категории',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.pk} | {self.name=}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Good(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=100,
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        verbose_name="Цена",
        decimal_places=2,
        max_digits=10,
    )
    image = models.ImageField(
        verbose_name="Картинка товара",
        null=True,
        blank=True,
        upload_to='goods/images'
    )
    available_quantity = models.IntegerField(
        verbose_name='Доступное количество',
        null=True,
        blank=True,
    )

    min_price = models.DecimalField(
        verbose_name="Цена со скидкой",
        decimal_places=2,
        max_digits=10,
        null=True,
        blank=True
    )
    subcategory = models.ForeignKey(
        "mainapp.SubCategory",
        on_delete=models.CASCADE,
        verbose_name="Подкатегория товара",
        related_name="goods"
    )
    is_active = models.BooleanField(
        verbose_name="Признак активности",
        default=True
    )

    def __str__(self):
        return f"{self.pk} | {self.name=}"

    def save(self, *args, **kwargs):
        try:
            old_obj = Good.objects.get(pk=self.pk)
        except Good.DoesNotExist:
            old_obj = None

        super().save(*args, **kwargs)

        if old_obj and old_obj.image and old_obj.image != self.image:
            old_image = old_obj.image.path
            default_avatar_name = None
            if os.path.isfile(old_image) and old_obj.image.url != default_avatar_name:
                os.remove(old_image)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class GoodInCart(models.Model):
    good = models.ForeignKey(
        'mainapp.Good',
        on_delete=models.CASCADE,
        verbose_name='Ссылка на товар',
    )
    quantity = models.IntegerField(
        verbose_name="Количество",
    )

    def __str__(self):
        return f"{self.pk} | {self.good.name=} | {self.quantity=}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


class Cart(models.Model):
    goods = models.ManyToManyField(
        "mainapp.GoodInCart",
        verbose_name="Корзина",
    )

    def __str__(self):
        user = getattr(self, 'user', None)
        return f"{self.pk} | {user}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
