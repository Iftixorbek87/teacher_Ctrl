from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:group_pk>/', views.student_add, name='student_add'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('toggle-task/', views.toggle_task, name='toggle_task'),
]
