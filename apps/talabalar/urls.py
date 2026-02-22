from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:guruh_pk>/', views.talaba_add, name='talaba_add'),
    path('<int:pk>/', views.talaba_detail, name='talaba_detail'),
    path('<int:pk>/edit/', views.talaba_edit, name='talaba_edit'),
    path('<int:pk>/delete/', views.talaba_delete, name='talaba_delete'),
    path('vazifa-toggle/', views.vazifa_toggle, name='vazifa_toggle'),
]
