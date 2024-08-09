from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    # user = request.user
    # account = user.bankaccount  # Assuming one-to-one relationship with User
    # context = {
    #     'user': user,
    #     'account_number': account.account_number,
    #     'balance': account.balance,
    # }
    return render(request, 'home.html')

@login_required
def account_details(request):
    user = request.user
    account = user.bankaccount  # Assuming one-to-one relationship with User
    context = {
        'user': user,
        'account_number': account.account_number,
        'balance': account.balance,
    }
    return render(request, 'account_details.html', context)

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Kullanıcı adı yada Şifre Hatalı"})
    else:
        return render(request, "login.html")

def register_request(request):
    return render(request, "register.html")

@login_required
def logout_request(request):
    logout(request)
    return redirect("login")
