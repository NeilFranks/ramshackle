from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
# from . import views


urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    # logout invalidates token; will need to login and get new token
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]
