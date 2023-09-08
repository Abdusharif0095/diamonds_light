from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.views import APIView
from .forms import CustomAuthenticationForm


class LoginView(APIView):
    def post(self, request):
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if user.is_superuser:
                        return redirect("/admin/")
                    if user.groups.filter(name="content-manager").exists():
                        return redirect("/admin/")
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("home")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")

    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request=request, template_name='authentication/login.html', context={"login_form": form})


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect("home")
