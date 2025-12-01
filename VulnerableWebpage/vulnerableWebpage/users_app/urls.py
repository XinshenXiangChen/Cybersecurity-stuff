from . import views
from django.urls import path

app_name = 'users_app'

urlpatterns = [
    path('login/', views.login, name='login'),
]