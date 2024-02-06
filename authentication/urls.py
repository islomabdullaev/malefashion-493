from django.urls import path
from authentication.views import signin

app_name = 'authentication'

urlpatterns = [
    path('signin/', signin, name='signin')
]
