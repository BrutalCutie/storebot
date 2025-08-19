from decimal import Decimal

from rest_framework import serializers

from mainapp.models import SubCategory, Category, Good, Cart, GoodInCart


class GoodSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.SerializerMethodField()

    class Meta:
        model = Good
        fields = "__all__"

    @staticmethod
    def get_subcategory_name(obj):
        return obj.subcategory.name


class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    goods = GoodSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = "__all__"

    @staticmethod
    def get_category_name(obj):
        return obj.category.name


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class GoodInCartSerializer(serializers.ModelSerializer):
    good = GoodSerializer(read_only=True)

    class Meta:
        model = GoodInCart
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    goods = GoodInCartSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    @staticmethod
    def get_total_price(obj):
        total_price = Decimal(0)

        for good in obj.goods.all():
            total_price += good.good.price * good.quantity

        return total_price

    class Meta:
        model = Cart
        fields = "__all__"
