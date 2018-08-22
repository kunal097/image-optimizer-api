from django.urls import path
from .views import index
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

path('api/',csrf_exempt(index))

]
