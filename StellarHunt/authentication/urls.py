from django.urls import path, include
from .views import *

app_name = 'authentication_api'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('check-username-email/', CheckUsernameEmailView.as_view(), name='check-username-email'),
]
