from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='main_paginate'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name = 'quote'),
    path('author/<str:fullname>/', views.author_about, name='author_fullname'),
]