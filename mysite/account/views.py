from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
# creating login view-->
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            login(request, user)
            return redirect("/home")

    else:
        form = AuthenticationForm(request)

    context = {"form": form}
    return render(request, "fooDonationApp\Accounts\login.html", context)


#  creating logout view
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")

    return render(request, "fooDonationApp\Accounts\logout.html", {})


# creating register view
def register_view(request):
    form = UserCreationForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        form.save()
        context["form"] = form
        return redirect("/login")

    return render(request, "fooDonationApp\Accounts\Register.html", context)


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)

#         if user is None:
#             context = {"error": "Invalid username and password"}
#             return render(request, "fooDonationApp\Accounts\login.html", context)

#         login(request, user)
#         return redirect("/home")

#     return render(request, "fooDonationApp\Accounts\login.html")
