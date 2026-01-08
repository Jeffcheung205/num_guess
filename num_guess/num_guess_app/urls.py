from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('new/', views.new_game, name='new_game'),
    path('play/', views.game_play, name='game_play'),
    path('end/', views.end_game, name='end_game'),
    path('stats/', views.game_stats, name='game_stats'),
]
