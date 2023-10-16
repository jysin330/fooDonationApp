from django.urls import path
from .views import home, donate, meals, search, Receive, About

urlpatterns = [
    path("About/", About),
    path("donate/", donate),
    path("home/", home),
    path("meals/", meals),
    path("Receive/", Receive),
    path("search/", search),
]
