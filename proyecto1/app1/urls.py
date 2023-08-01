from django.urls import path
from . import views

urlpatterns = [
    path('probando_template/', views.probando_template, name="probando_template")
]