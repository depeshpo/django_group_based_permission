from django.urls import path

from .views import UserListView, UserCreateView, UserDeleteView, UserUpdateView, search

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('users/add/', UserCreateView.as_view(), name='add-user'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='update-user'),
    path('users/search/', search, name='search-users')
]
