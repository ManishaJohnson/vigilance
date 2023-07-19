from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register,name='register'),
    path('admin_login/', views.admin,name='admin'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('profile/', views.profile,name='admin-profile'),
    path('create_admin/', views.new_admin,name='admin-creation'),
    path('update/', views.update_info,name='info-update'),
    path('delete/', views.delete,name='delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )