from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
	path('games/<visited>', views.ListGamesAPIView.as_view(), name = 'ListGames'),
	path('game/<slug>', views.SingleGameAPIView, name = 'SingleGame'),
	path('game/<slug>/take_part',views.GameTakePartAPIView, name = 'GameTakePartAPIView'),
	path('game/<slug>/start', views.StartGameAPIView, name = 'StartGame'),
	path('game/<slug>/close_check_point', views.CloseCheckPointAPIView, name = 'CloseCheckPoint'),
	path('game/<slug>/join_team/<token>',views.JoinTeamAPIView, name = 'JoinTeam'),
	path('register', views.UserRegisterAPIView, name = 'UserRegister'),
	path('login', obtain_auth_token, name = 'UserLogin'),
	path('logout', views.UserLogoutAPIView, name = 'UserLogout'),
	path('activate/<uidb64>/<token>', views.UserActivationAPIView, name = 'UserActivation'),
	path('reset_password_request', views.UserResetPasswordRequestAPIView, name = 'UserResetPasswordRequest'),
	path('reset_password/<uidb64>/<token>', views.UserResetPasswordAPIView, name = 'UserResetPassword'),
]
