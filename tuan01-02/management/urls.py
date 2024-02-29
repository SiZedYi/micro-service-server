from django.contrib import admin
from django.urls import path
from .api.user import  RegisterView,LoginView
from .api.list_and_detail_obj import ListProductView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    #Auth
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('jwt/create', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify', TokenVerifyView.as_view(),name='token_verify'),

    #List and Get Detail
    path('list-product', ListProductView.as_view(), name='list-dia-phuong'),


]
