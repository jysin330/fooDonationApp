from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        login(request, user)

        return redirect("/login")

    return render(request, "fooDonationApp\Accounts\login.html")
