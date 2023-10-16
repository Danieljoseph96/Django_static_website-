from django.urls import path 
from pages import views

urlpatterns = [
    path("",views.home,name=''),
    path("about/",views.About,name='contact'),
]sss