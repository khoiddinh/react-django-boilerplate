from django.shortcuts import render

# Example view
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Note: add views to config/urls.py
@api_view(["GET"])
def hello(request):
    return Response({"message": "Hello World"})

# Create your views here.
