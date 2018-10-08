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
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
import requests
import math
# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes, renderer_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication

from django.utils.crypto import get_random_string
redis_con = redis.StrictRedis(host="localhost", port="6379", db="0")


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes((AllowAny,))
@login_required(login_url='/login/')
def EMITemplate(request):
    return Response({'template':'emicalc'},template_name='emi_page.html')

@api_view(['GET'])
@permission_classes((AllowAny,))
@login_required(login_url='/login/')
def emiCalculate(request):
    try:
        json_data = {}
        principal = request.GET.get('principal')
        rate = request.GET.get('interest')
        duration = request.GET.get('duration')
        startMonth = request.GET.get('startMonth')
        startYear = request.GET.get('startYear')
        durationType = request.GET.get('durationType')
        monthNames = ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"]
        monthDict = {}
        loanDict = {}
        if principal and rate and duration and startMonth and startYear and durationType:
            principal = float(principal)
            rate = float(rate)
            duration = float(duration)
            if durationType=="Y" :
                duration = duration * 12;
            rate = float((rate/12)/100)
            ratePower = float(math.pow((1+rate),duration))
            emi = float(principal*rate*(ratePower/(ratePower -1)))
            InterestPay =  float((emi*duration)-principal)
            totalPay = float(principal + InterestPay)
            for i in range(1,int(duration)+1):
                interstRateMonth = float(rate) * float(principal)
                principalMonth = float(emi) - float(interstRateMonth)
                loanRepaid = (principalMonth *100)/float(principal)
                principal = float(principal) - principalMonth;   
                totalVal = {'Principal':round(principalMonth) ,'Interest':round(interstRateMonth) , 'Total Payment':round(emi),'Balance':round(principal),'Loan Paid':round(loanRepaid)}
                monthName = monthNames[int(startMonth) - 1]
                monthDict[monthName] = totalVal
                loanDict[startYear] = monthDict
                if int(startMonth) == 12:
                    monthDict = {}
                    startMonth = 0;
                    startYear  = int(startYear)  + 1;
                startMonth = int(startMonth) + 1;
            json_data['loandata'] = loanDict
            json_data['totalPay'] = round(totalPay)
            json_data['status'] = "Success"
        else:
            json_data['status'] = "Failed"
    except Exception as e:
        json_data['status'] = "exception"
        json_data['exception'] = e
    return Response(json_data)