from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.patoklar import views as patok_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', patok_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('patoklar/', include('apps.patoklar.urls')),
    path('guruhlar/', include('apps.guruhlar.urls')),
    path('talabalar/', include('apps.talabalar.urls')),
]
