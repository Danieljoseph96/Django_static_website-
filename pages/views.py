from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'pages/home.html',{})

def About(request):
    return render(request, 'pages/about.html',{})