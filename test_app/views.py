from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"message": "Very very ready to start!"})