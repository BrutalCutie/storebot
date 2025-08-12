from django.urls import path
from rest_framework.routers import DefaultRouter

from mainapp.apps import MainappConfig
from . import views

app_name = MainappConfig.name

router = DefaultRouter()
router.register(r'subcategories', views.SubCategoryViewSet, basename='subcategories')
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'goods', views.GoodViewSet, basename='goods')


urlpatterns = [

] + router.urls

