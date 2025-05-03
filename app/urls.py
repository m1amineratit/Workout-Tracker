from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='home'),
    path('workout/', views.record_work, name='add_workout'),
    path('update-workout/', views.update_workout, name='update_workout'),
    path('delete-workout/<int:pk>/', views.delete_workout, name='delete_workout'),
]