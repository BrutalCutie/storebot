from django.urls import path
from rest_framework.routers import DefaultRouter

from mainapp.apps import MainappConfig
from . import views

app_name = MainappConfig.name

router = DefaultRouter()
router.register(r'api/subcategories', views.SubCategoryViewSet, basename='subcategories')
router.register(r'api/categories', views.CategoryViewSet, basename='categories')
router.register(r'api/goods', views.GoodViewSet, basename='goods')


urlpatterns = [

    path('', views.HomeTemplateView.as_view(), name='home')

] + router.urls

