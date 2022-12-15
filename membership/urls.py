from django.urls import path
from . import views

urlpatterns = [
    path('membership/login/', views.login_user_view, name="login"),
    path('membership/logout/', views.logout_user_view, name="logout"),
    path('membership/register/', views.register_user_view, name="register"),
    path('membership/register_admin/', views.register_moderator_view, name="register_admin")
]