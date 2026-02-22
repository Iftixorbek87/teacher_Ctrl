from django.urls import path
from . import views

urlpatterns = [
    path('', views.patok_list, name='patok_list'),
    path('create/', views.patok_create, name='patok_create'),
    path('<int:pk>/', views.patok_detail, name='patok_detail'),
    path('<int:pk>/edit/', views.patok_edit, name='patok_edit'),
    path('<int:pk>/delete/', views.patok_delete, name='patok_delete'),
]
