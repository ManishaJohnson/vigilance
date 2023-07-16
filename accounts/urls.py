from django.urls import path,include
from . import views
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
