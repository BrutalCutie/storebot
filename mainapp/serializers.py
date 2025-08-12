from rest_framework import serializers

from mainapp.models import SubCategory, Category, Good


class GoodSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.SerializerMethodField()

    class Meta:
        model = Good
        fields = "__all__"

    def get_subcategory_name(self, obj):
        return obj.subcategory.name


class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    goods = GoodSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = "__all__"

    def get_category_name(self, obj):
        return obj.category.name


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
