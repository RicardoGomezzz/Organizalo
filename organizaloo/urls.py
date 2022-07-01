from django.urls import path
from organizaloo.views import index
from re import A



urlpatterns = [
    path('index/', index,name='index'),
]