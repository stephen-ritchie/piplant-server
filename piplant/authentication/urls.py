from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('login', views.UserLoginFormView.as_view(), name='login')
]
