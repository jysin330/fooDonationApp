from django.urls import path
from .views import (
    home,
    donate,
    meals,
    search,
    history,
    Receive,
    About,
    meals_detail,
    request_meal,
)

urlpatterns = [
    path("About/", About),
    path("donate/", donate),
    path("home/", home),
    path("meals/", meals),
    path("meals/<int:id>", meals_detail),
    path("request_meal/", request_meal),
    path("Receive/", Receive),
    path("search/", search),
    path("history/", history),
]
