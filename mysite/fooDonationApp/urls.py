from django.urls import path
from .views import (
    home,
    cookedFood,
    donate,
    meals,
    packedFood,
    search,
    history,
    Receive,
    About,
    meals_detail,
    request_meal,
    rawFood,
)

urlpatterns = [
    path("About/", About),
    path("CookedFood/", cookedFood),
    path("donate/", donate),
    path("home/", home),
    path("history/", history),
    path("meals/", meals),
    path("meals/<int:id>", meals_detail),
    path("PackedFood/", packedFood),
    path("request_meal/", request_meal),
    path("Receive/", Receive),
    path("RawFood/", rawFood),
    path("search/", search),
]
