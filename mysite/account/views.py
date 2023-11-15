from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error": "Invalid username and password"}
            return render(request, "fooDonationApp\Accounts\login.html", context)

        login(request, user)
        return redirect("/home")

    return render(request, "fooDonationApp\Accounts\login.html")
