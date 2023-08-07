from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.


class HomeView(APIView):
    def get(self, request):
        return HttpResponse("<h1>Welcome to Diamond's Light</h1>")
