from django.urls import path
from .views import login_request, logout_request, register_request, test_request, staff_register_request

urlpatterns = [ 
    # path('accounts/signup/', home.SignUpView.as_view(), name='signup'),s
    path('signup/',  register_request, name='consumer_signup'),
    path('staff/', staff_register_request, name='staff_signup'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('test/', test_request, name='test'),
]