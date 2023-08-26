from django.urls import path

from .views import LoginView, LogoutView, SignupView

app_name = 'authentication_api'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
