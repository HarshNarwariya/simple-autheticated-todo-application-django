from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', view=auth_views.LoginView.as_view(
        template_name="Accounts/login.html",
        redirect_authenticated_user=True,
    ), name="login"),
    path('logout/', view=auth_views.LogoutView.as_view(
        template_name="Accounts/logout.html",
    ), name="logout"),
    path('signup/', view=views.register, name="signup"),
]