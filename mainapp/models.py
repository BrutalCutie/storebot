from django.db import models


class SubCategory(models.Model):
    name = models.CharField(
        verbose_name="Наименование подкатегории",
        max_length=100,
    )
    help_text = models.TextField(
        verbose_name='Подробности подкатегории',
    )

    def __str__(self):
        return f"{self.pk} | {self.name=}"


class Category(models.Model):
    name = models.CharField(
        verbose_name="Наименование категории",
        max_length=100,
    )
    help_text = models.TextField(
        verbose_name='Подробности категории',
    )
    sub_category = models.ManyToManyField(
        "mainapp.SubCategory",
        verbose_name="Подкатегории",
        related_name="subcategories"
    )

    def __str__(self):
        return f"{self.pk} | {self.name=}"


class Good(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=100,
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    price = models.DecimalField(
        verbose_name="Цена",
        decimal_places=2,
        max_digits=10,
    )
    min_price = models.DecimalField(
        verbose_name="Цена со скидкой",
        decimal_places=2,
        max_digits=10,
    )
    subcategory = models.ForeignKey(
        "mainapp.SubCategory",
        on_delete=models.CASCADE,
        verbose_name="Подкатегория товара",
        related_name="goods"
    )

    def __str__(self):
        return f"{self.pk} | {self.name=}"


class Cart(models.Model):
    goods = models.ManyToManyField(
        "mainapp.Good",
        verbose_name="Корзина",
    )

