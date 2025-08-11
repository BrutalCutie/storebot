from rest_framework.viewsets import ModelViewSet

from .models import SubCategory, Category
from .serializers import SubCategorySerializer, CategorySerializer


class SubCategoryViewSet(ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

