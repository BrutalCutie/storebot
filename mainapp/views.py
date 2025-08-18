from django.db.models import Prefetch
from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet

from .models import SubCategory, Category, Good, Cart
from .serializers import SubCategorySerializer, CategorySerializer, GoodSerializer, CartSerializer


class SubCategoryViewSet(ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = (SubCategory.objects
                .select_related('category')
                .prefetch_related('goods')
                .all())


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.prefetch_related(Prefetch(
        'subcategories', queryset=SubCategory.objects.prefetch_related("goods").all()
    )).all()


class GoodViewSet(ModelViewSet):
    serializer_class = GoodSerializer
    queryset = Good.objects.select_related("subcategory").all()


class CartDetailView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class HomeTemplateView(TemplateView):
    template_name = 'mainapp/main.html'
