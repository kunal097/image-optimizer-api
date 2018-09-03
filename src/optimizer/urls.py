from django.urls import path
from .views import index , home


urlpatterns = [

path('api/',home),
path('',index,name='home')

]
