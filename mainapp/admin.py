from django.contrib import admin

from mainapp.models import Good, Category, SubCategory


@admin.register(Good)
class AdminGood(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "subcategory",
        "price",
        "min_price",
    )
    list_filter = (
        "id",
        "name",
        "subcategory",
        "price",
        "min_price",
    )
    search_fields = (
        "name",
    )


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = (
        "id",
        "name",
        )
    search_fields = (
        "name",
    )


@admin.register(SubCategory)
class AdminSubCategory(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = (
        "id",
        "name",
        )
    search_fields = (
        "name",
    )


