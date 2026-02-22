from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.groups import views as group_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', group_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('groups/', include('apps.groups.urls')),
    path('students/', include('apps.students.urls')),
]
