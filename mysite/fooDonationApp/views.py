from django.shortcuts import render
from .models import Donate


# Create your views here.
def home(request):
    return render(request, "fooDonationApp\home.html")


def About(request):
    return render(request, "fooDonationApp\About.html")


def donate(request):
    # post request --->
    if request.method == "POST":
        donarName = request.POST.get("fname")
        category = request.POST.get("Category")
        donarEmail = request.POST.get("email")
        donarPhone = request.POST.get("phoneNum")
        foodItem = request.POST.get("FoodName")
        des = request.POST.get("description")
        donarAddress = request.POST.get("address")
        foodImage = request.POST.get("foodImage")
        # print(donarEmail, donarName, donarPhone, foodItem)

        Donate.objects.create(
            category=category,
            donarName=donarName,
            donarEmail=donarEmail,
            phoneNum=donarPhone,
            foodItem=foodItem,
            fooDescription=des,
            address=donarAddress,
            image=foodImage,
        )
    return render(request, "fooDonationApp\donate.html")


def meals(request):
    return render(request, "fooDonationApp\meals.html")


def Receive(request):
    return render(request, "fooDonationApp\Receive.html")


def search(request):
    return render(request, "fooDonationApp\search.html")


def history(request):
    return render(request, "fooDonationApp\history.html")
