from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('create/',views.post_created,name="create"),
    
]