from django.urls import path
from . import views

urlpatterns= [
          path('', views.index, name='suryash'),
          path('result/', views.result, name='result'),
        ]
