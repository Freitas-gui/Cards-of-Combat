from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, my_logout


urlpatterns = [
    path('', home, name = "url_home"),
    path('login/', auth_views.LoginView.as_view(), name='url_login'),
    path('logout/', my_logout, name='url_logout'),


]