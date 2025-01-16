from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make-payment/', views.make_payment, name='make_payment'),
]