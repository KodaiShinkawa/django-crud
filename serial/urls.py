from django.urls import path
from . import views


urlpatterns = [
    path('serial/', views.SerialView.as_view(), name='serial-home'),
]
