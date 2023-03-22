from django.urls import path
from .views import ProfileView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    path('profile/',ProfileView.as_view()) 
]
urlpatterns = format_suffix_patterns(urlpatterns)