from django.urls import path      
from .views import new_response

urlpatterns = [
    path('',new_response)
]