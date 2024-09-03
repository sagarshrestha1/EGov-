from django.urls import path
from . import views

urlpatterns = [
    path('', views.listComplaints, name='index'),
    path('submit', views.index, name='complaint'),
    path('signup/', views.signup, name='signup')
]