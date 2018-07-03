# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
from django.conf import settings
import redis
import ast
from django.contrib.auth.models import User 
# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.utils.crypto import get_random_string
redis_con = redis.StrictRedis(host="localhost", port="6379", db="0")

@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
def login(request):
    return Response({'template':'login'},template_name='login.html')

@api_view(['POST'])
def user_register(request):
    dict_data = {}
    data = request.data
    dict_data.update(request.data)
    subject = """Builder Hut account activation link"""
    unique_id = get_random_string(length=32)
    if unique_id in redis_con.keys():
        del redis_con[unique_id]
    html = """\
            <html>
              <head></head>
              <body>
                <p>Hi! """+ request.POST.get('username')+"""<br>
                    Welcome to Builder Hut and thank you for registering with us.<br>
                    To activate your account please verify your email address by clicking the link below:<br>
                    <a href='http://192.168.11.73:8000/login/account_verify/"""+unique_id+"""'>Activate your account</a><br>
                    Please activate your account within 2 days. All future notifications will be sent to this email address.<br>
                    Thank You for choosing Builder Hut!<br>
                </p>
              </body>
            </html>
            """
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        s = serializer.save()
        dict_data.update({'id':s.id})
        redis_con.set(unique_id,dict_data)
        print redis_con.get(unique_id)
        sendMessage(request.POST.get('email'),subject,html)
        return Response({"message": "User created"}) 
    else:
        data = {
          "error": True,
          "errors": serializer.errors,          
        }
        return Response(data)
    
@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
def user_activate(request,token):
    data = {}
    if token in redis_con.keys():
        restoken = ast.literal_eval(redis_con[token])
        User.objects.filter(pk=restoken['id']).update(is_active=True)
        del redis_con[token]
        data = {'status':1,'message':"Your Account has been verified"}
    else:
        data = {'status':0,'message':"Verification Failed"}
    return Response(data,template_name='login.html')
    

def sendMessage(email_to,email_subject,html):
    msg = MIMEMultipart()
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = email_to
    msg['Subject'] = email_subject
    msg.attach(MIMEText(html, 'html'))
    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    text = msg.as_string()
    server.sendmail(settings.EMAIL_HOST_USER, email_to, text)

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