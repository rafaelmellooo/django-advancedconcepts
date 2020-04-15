from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users/new/', views.new, name="new-user"),
    path('users/<slug:slug>/', views.detail, name="user"),
    path('users/<slug:slug>/update/', views.update, name="update-user"),
    path('users/<slug:slug>/delete/', views.delete, name="delete-user")
]
