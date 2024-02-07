from django.urls import path
from authentication.views import signin, signout, signup

app_name = 'authentication'

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup')
]
