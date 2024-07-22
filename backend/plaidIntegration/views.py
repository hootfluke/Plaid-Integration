from django.shortcuts import render
from rest_framework import viewsets
from .serialize import plaidUserSerializer
from .models import plaidUser

# Create your views here.

class plaidUserView(viewsets.ModelViewSet):
    serializer_class = plaidUserSerializer
    queryset = plaidUser.objects.all()
