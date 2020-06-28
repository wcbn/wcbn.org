from django.urls import path
from .views import *

app_name = 'wcbn_auth'
urlpatterns = [
    # path('profile', ProfileView.as_view(), name='profile'),
    # path('profile/update', ProfileUpdateView.as_view(), name='update_profile'),
    # path('users/<int:pk>', UserDetailView.as_view(), name='detail_user'),
    # path('users/<int:pk>/update', UserUpdateView.as_view(), name='update_user'),
    path('users/login/', WCBNLoginView.as_view(), name='login'),
    path('users/create', UserCreateView.as_view(), name='create_user'),
]
