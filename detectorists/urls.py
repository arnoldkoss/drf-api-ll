from django.urls import path
from detectorists import views

urlpatterns = [
    path('detectorists/', views.DetectoristList.as_view()),
    path('detectorists/<int:pk>/', views.DetectoristDetail.as_view()),
]