from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('user', views.user, name='user'),
    path('logouts', views.logouts, name='logouts'),
    path('post-for-recruitment', views.postJob,name='recruitment'),
    path('update', views.updateData,name='updateData'),
    path('apply/<jobPostID>', views.apply,name='applyJob'),
    # path('apply', views.postJob),
    path('<userID>', views.userProfile, name='userprofile'),
]
