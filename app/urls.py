from django.urls import path
from .views.auth import login, register, logout
from .views.main import home, leaderboard

urlpatterns = [
    
    # Authentication
    path('auth/login/',login.LoginTemplate,name='login'),
    path('auth/register/',register.RegisterTemplate,name='register'),
    path('auth/logout/',logout.LogoutView,name='logout'),

    path('',home.HomeTemplate,name='home'),
    path('leaders/',leaderboard.LeaderBoardTemplate,name='leaders'),

]
