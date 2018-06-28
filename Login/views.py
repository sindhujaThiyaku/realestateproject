# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
def login(request):
    return Response(template_name='login.html')

@api_view(['POST'])
def user_register(request):
    print "*******************",request.POST
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"}) 
    else:
        data = {
          "error": True,
          "errors": serializer.errors,          
        }
        return Response(data)

# @api_view(["POST"])
# def create_user(request):
#     serializer = UserSerializer(request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "User created"}) 
#     else:
#         data = {
#           "error": True,
#           "errors": serializer.errors,          
#         }
#         return Response(data)  

# class LoginDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'login.html'
#     def get(self, request, *args, **kwargs):
#         return Response(template_name=self.template_name)

# class dashboardDetail(APIView):
    
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'index.html'
#     def get(self, request, *args, **kwargs):
#         return Response(template_name=self.template_name)

# class aboutUsView(APIView):
    
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'about.html'
#     def get(self, request, *args, **kwargs):
#         return Response(template_name=self.template_name)

# class listingsView(APIView):
    
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'listings.html'
#     def get(self, request, *args, **kwargs):
#         return Response(template_name=self.template_name)

# class listingsSingleView(APIView):
    
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'listings_single.html'
#     def get(self, request, *args, **kwargs):
#         return Response(template_name=self.template_name)

# class newsView(APIView):
    
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'news.html'
#     def get(self, request, *args, **kwargs):
#         return Response(template_name=self.template_name)

# class contactView(APIView):
    
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'contact.html'
#     def get(self, request, *args, **kwargs):
#         return Response(template_name=self.template_name)
