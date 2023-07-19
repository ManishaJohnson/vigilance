from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.gp_home,name='public'),
    path('burglary', views.burglary,name='crime-burglary'),
    path('map', views.districtMap,name='district-map'),
    path('arms_map', views.arms_districtMap,name='crime-arms'),
   	path('gambling', views.gambling_districtMap,name='crime-gambling'),
   	path('mining', views.mining_districtMap,name='crime-mining'),
   	path('trafficking', views.traffic_districtMap,name='crime-traffic'),
   	path('goonda', views.goonda_districtMap,name='crime-goonda'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )