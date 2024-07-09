from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from drf.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/listcreatepoet/', ListCreatePoet.as_view()),
    path('api/v1/updatepoet/<int:pk>/', UpdataPoet.as_view()),
    path('api/v1/retrivedeletepoet/<int:pk>/', DeleteRetrivePoet.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]