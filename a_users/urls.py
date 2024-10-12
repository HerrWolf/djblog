from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/<username>/', profile_view, name='userprofile'),
    path('profile/edit/', profile_edit_view, name='profile-edit'),
    path('profile/onboarding/', profile_edit_view, name='profile-onboarding'),
    path('profile/delete/', profile_delete_view, name='profile-delete'),
]