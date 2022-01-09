from django.urls import path

from . import views

urlpatterns = [
    path('newuser', views.NewUserFormView.as_view(), name='newuser'),
    path('', views.home, name='home'),
    path('profile', views.profile_view, name='profile')
    # path('login', views.login),
]