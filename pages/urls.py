from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    contact_view
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', contact_view, name='contacts'),
]