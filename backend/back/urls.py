from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
	path('games', views.ListGamesAPIView.as_view(), name = 'ListGames'),
	path('game/<slug>', views.SingleGameAPIView.as_view(), name = 'SingleGame'),
	# path('game/<slug>/take_part',),
	path('register', views.UserRegisterAPIView, name = 'UserRegister'),
	path('login', obtain_auth_token, name = 'UserLogin'),
	path('logout', views.UserLogoutAPIView, name = 'UserLogout'),
	path('activate/<uidb64>/<token>', views.UserActivationAPIView, name = 'UserActivation'),
	path('reset_password_request', views.UserResetPasswordRequestAPIView, name = 'UserResetPasswordRequest'),
	path('reset_password/<uidb64>/<token>', views.UserResetPasswordAPIView, name = 'UserResetPassword'),
]
