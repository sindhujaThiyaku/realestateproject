# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        return Response(template_name=self.template_name)

class dashboardDetail(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return Response(template_name=self.template_name)

class aboutUsView(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'about.html'
    def get(self, request, *args, **kwargs):
        return Response(template_name=self.template_name)

class listingsView(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'listings.html'
    def get(self, request, *args, **kwargs):
        return Response(template_name=self.template_name)

class listingsSingleView(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'listings_single.html'
    def get(self, request, *args, **kwargs):
        return Response(template_name=self.template_name)

class newsView(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'news.html'
    def get(self, request, *args, **kwargs):
        return Response(template_name=self.template_name)

class contactView(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contact.html'
    def get(self, request, *args, **kwargs):
        return Response(template_name=self.template_name)
