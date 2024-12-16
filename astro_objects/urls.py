from django.urls import path, include
from astro_objects import views




urlpatterns = [
    path('api/astro_objects/', views.AstronomicalObjectListView.as_view(), name='astro_objects_list'),
    path('api/astro_objects/<int:pk>', views.AstronomicalObjectDetailView.as_view(), name='astronomicalobject-detail'),
    path('', views.api_root,name='api_root'),
    
]
