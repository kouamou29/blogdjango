from django.urls import path

from src import views

urlpatterns = [
   path('', views.index, name='index'),
   path('formblog/', views.formblog, name="formblog"),
   path('editblog/<str:pk>/', views.editblog, name='editblog'),
   path('deleteblog/<str:pk>/', views.deleteblog, name='deleteblog'),
]
