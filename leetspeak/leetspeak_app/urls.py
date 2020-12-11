from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<str:string>", views.api, name="api"),
]
