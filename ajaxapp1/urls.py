from django.urls import path
from . import views


urlpatterns = [
    path('ajax_url/', views.ajax_view, name='ajax-url'), #ajax url
    path('index/', views.index, name='index'), #ajax call url
]
