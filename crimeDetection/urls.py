from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='app-home'),
    path('services/', views.services,name='services-page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )