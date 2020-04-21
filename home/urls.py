from django.urls import path , include
from home import urls as home_urls
from .views import home, my_logout

urlpatterns = [
    path('', home, name = "url_home"),
    path('logout/', my_logout, name='url_logout'),

]