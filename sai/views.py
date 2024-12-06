from django.shortcuts import render

# Create your views here.

def guts(request):
    return render(request,'power.html')