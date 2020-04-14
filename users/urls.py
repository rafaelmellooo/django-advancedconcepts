from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new-user"),
    path('<slug:slug>/', views.detail, name="user"),
    path('<slug:slug>/update/', views.update, name="update-user"),
    path('<slug:slug>/delete/', views.delete, name="delete-user")
]
