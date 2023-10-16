from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "fooDonationApp\home.html")


def About(request):
    return render(request, "fooDonationApp\About.html")


def donate(request):
    return render(request, "fooDonationApp\donate.html")


def meals(request):
    return render(request, "fooDonationApp\meals.html")


def category(request):
    return render(request, "fooDonationApp\category.html")


def Receive(request):
    return render(request, "fooDonationApp\Receive.html")


def search(request):
    return render(request, "fooDonationApp\search.html")
