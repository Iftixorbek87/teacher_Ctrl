from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:patok_pk>/', views.guruh_create, name='guruh_create'),
    path('<int:pk>/', views.guruh_detail, name='guruh_detail'),
    path('<int:pk>/edit/', views.guruh_edit, name='guruh_edit'),
    path('<int:pk>/delete/', views.guruh_delete, name='guruh_delete'),
    path('<int:pk>/vazifa-soni/', views.guruh_vazifa_soni, name='guruh_vazifa_soni'),
]
