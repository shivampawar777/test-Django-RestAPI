from django.urls import path
from app.views import index, person


urlpatterns = [
    path('index/', index),
    path('person/', person)
]
