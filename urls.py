from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from apps import views



urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('shubh/', views.shubh),


]
