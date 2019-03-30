"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todos.views import crear_tarea, TareaViewSet

api_router = DefaultRouter(trailing_slash=False)
api_router.register('todos', TareaViewSet, base_name='todos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos', crear_tarea),
    path('api/todos/<int:id>', crear_tarea),
    path('api/v1/', include(api_router.urls)),
]
