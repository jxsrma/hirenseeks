from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login'),
    path('user', views.user, name = 'user'),
    path('logouts', views.logouts, name = 'logouts')
]

