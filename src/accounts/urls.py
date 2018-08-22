from django.urls import path
from .views import LoginView,RegisterView,LogoutView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('login/', csrf_exempt(LoginView.as_view()) , name = "login"),
    path('register/', RegisterView.as_view() , name = "register"),
    path('logout/', LogoutView.as_view() , name = "logout"),

]
