from django.urls import path
from .views import *
 
urlpatterns = [
    path('', home),
    path('example/', example),
    path('buble/', buble),
    path('new/', new)

]