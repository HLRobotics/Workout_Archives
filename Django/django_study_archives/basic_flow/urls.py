from django.urls import path
from basic_flow import views

urlpatterns=[
    path('',views.load_subpage),
]