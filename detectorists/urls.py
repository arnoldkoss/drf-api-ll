from django.urls import path
from detectorists import views

urlpatterns = [
    path('detectorists/', views.DetectoristList.as_view()),
]