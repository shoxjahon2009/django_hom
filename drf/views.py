from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Person, Category
from .permission import IsAdminUserOrReadOnly, IsOwnerUserOrReadOnly
from .serializers import PoetSerializers




class ListCreatePoet(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PoetSerializers
    permission_classes = [IsAuthenticated]

class UpdataPoet(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PoetSerializers
    permission_classes = (IsOwnerUserOrReadOnly, )



class DeleteRetrivePoet(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PoetSerializers
    permission_classes = (IsAuthenticated,)