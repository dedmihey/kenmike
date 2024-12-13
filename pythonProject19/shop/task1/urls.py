"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# import sys
# import os
# sys.path.append(os.path.join(os.getcwd(), ".."))
# from .views import index, index2
from .views import index11, index12, index13
from .views import sign_up_by_django, sign_up_by_html
from .views import news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_up_by_html),
    # path('index/', index2.as_view()),
    path('haupt/', index11),
    path('haupt/kesseln/', index12),
    path('haupt/korb/', index13),
    path('django_sign_up/', sign_up_by_django),
    path('platform/news/', news),
]
