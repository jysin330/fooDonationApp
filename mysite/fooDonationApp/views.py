from django.shortcuts import render
from .models import Donate, ReceiverUser
from .form import DonateForm, ReceiveForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "fooDonationApp\home.html")


def About(request):
    return render(request, "fooDonationApp\About.html")


@login_required
def donate(request):
    form = DonateForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        donate_object = form.save()
        context["form"] = DonateForm()
        context["object"] = donate_object
        context["created"] = True
    return render(request, "fooDonationApp\donate.html", context)


def meals(request):
    meal_object = Donate.objects.all()
    # meal_query = meal_object

    obj = {"object": meal_object}

    obj["list"] = [["Raw Food","rawFood"],["Packed Food","packedFood"], ["Cooked Food","cookedFood"]]
    return render(request, "fooDonationApp\meals.html", obj)

#  The overall Donated Food BY Donar User
def meals_detail(request, id):
    meal_object = Donate.objects.all().filter(id=id)
    # meal_query = meal_object
    # print(meal_object)
    obj = {"object": meal_object}
    return render(request, "fooDonationApp\details\meal_detail.html", obj)

#  requesting meal from the page (by recieverUser request)
def request_meal(request):
    form = ReceiveForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        receive_object = form.save()
        context["form"] = ReceiveForm()
        context["object"] = receive_object
        context["created"] = True

    return render(request, "fooDonationApp\details\Request_form.html", context)

def rawFood(request):
    meal_object = Donate.objects.filter(category = 'Raw Food')
    context ={
        "object" : meal_object
    }
    return render(request, "fooDonationApp\details\RawFooDetail.html", context= context)

def cookedFood(request):
    meal_object = Donate.objects.filter(category = "Cooked Food")
    context= {
        "object": meal_object
    }
    return render(request,  "fooDonationApp\details\cookedFooDetail.html", context)

def packedFood(request):
    meal_object = Donate.objects.filter(category = "Packed Food")
    context ={
        "object": meals_detail
    }
    return render(request,  "fooDonationApp\details\packedFooDetail.html",context)

def Receive(request):
    return render(request, "fooDonationApp\Receive.html")


def search(request):
    # converting query into integer either none
    try:
        query = int(request.GET.get("query"))
    except:
        query = None

    item_obj = None
    if query is not None:
        item_obj = Donate.objects.get(id=query)

    else:
        item_obj = {}
    context = {"object": item_obj}
    return render(request, "fooDonationApp\search.html", context)


def history(request):
    return render(request, "fooDonationApp\history.html")


#  oldd----->
# @login_required
# def donate(request):
#     form = DonateForm()
#     context = {"form": form}
#     # post request --->
#     if request.method == "POST":
#         form = DonateForm(request.POST or None)
#         if form.is_valid():
#             donarName = form.cleaned_data.get("donarName")
#             category = form.cleaned_data.get("category")
#             donarEmail = form.cleaned_data.get("donarEmail")
#             phoneNum = form.cleaned_data.get("phoneNum")
#             foodItem = form.cleaned_data.get("foodItem")
#             fooDescription = form.cleaned_data.get("fooDescription")
#             address = form.cleaned_data.get("address")

#             # print(donarEmail, donarName, donarPhone, foodItem)

#             donate_object = Donate.objects.create(
#                 category=category,
#                 donarName=donarName,
#                 donarEmail=donarEmail,
#                 phoneNum=phoneNum,
#                 foodItem=foodItem,
#                 fooDescription=fooDescription,
#                 address=address,
#             )
#             context["object"] = donate_object
#             context["created"] = True
#     return render(request, "fooDonationApp\donate.html", context)

# def request_meal(request):

# meal_object = Donate.objects.all().filter(id=id)
# if request.method == "POST":
#     receiver_meal = request.POST.get("foodItemName")
#     receiver_name = request.POST.get("receiverName")
#     receiver_email = request.POST.get("receiverEmail")
#     receiver_num = request.POST.get("receiverNumber")
#     receiver_address = request.POST.get("receiverAddress")
#     des = request.POST.get("receivertext")
#     b = ReceiverUser(
#         receiver_meal=receiver_meal,
#         receiver_name=receiver_name,
#         receiver_email=receiver_email,
#         receiver_num=receiver_num,
#         receiver_address=receiver_address,
#         des=des,
#     )
#     b.save()
# context["object"] = meal_object
# context["created"] = True
# context = {"object": meal_object, "created": True}

# return render(request, "fooDonationApp\details\Request_form.html", context)
