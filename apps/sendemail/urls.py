
from django.urls import path
from apps.sendemail import views

urlpatterns = [
   
	path('register/', views.Registro.as_view(), name = 'register'),
	path('send/', views.send, name='send'),


]