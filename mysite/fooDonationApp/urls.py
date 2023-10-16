from django.urls import path
from .views import home, donate, meals, search, category, Receive, About

urlpatterns = [
    path("category/", category),
    path("About/", About),
    path("donate/", donate),
    path("home/", home),
    path("meals/", meals),
    path("Receive/", Receive),
    path("search/", search),
]
