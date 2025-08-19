from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from mainapp.models import Cart
from users.models import User
from users.serializers import UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'tg_id'

    def get_queryset(self):
        return User.objects.select_related('cart').all()

    def get_object(self):
        tg_id = self.kwargs['tg_id']
        user = User.objects.filter(tg_id=tg_id).first()
        if not user.cart:
            user.cart = Cart.objects.create()
            user.save()

        return super().get_object()

