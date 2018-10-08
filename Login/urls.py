"""realestateproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.loginTemplate, name="login render"),
    url(r'^user_register/$', views.user_register, name="user register"),
    url(r'^account_verify/(?P<token>[\w-]+)/$', views.user_activate, name="account_verify"),
    url(r'^user_login/', views.user_login, name='user_login'),
    # url(r'^dashboard/', dashboardDetail.as_view(), name='dashboard'),
    # url(r'', LoginDetail.as_view(), name='loginForm'),
    
    # url(r'^listings/', listingsView.as_view(), name='listings'),
    # url(r'^listingssingle/', listingsSingleView.as_view(), name='listingsSingle'),
    # url(r'^contactus/', newsView.as_view(), name='contactus'),
    # url(r'^news/', contactView.as_view(), name='news'),
]