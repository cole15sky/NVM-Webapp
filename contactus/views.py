from django.shortcuts import render

def contactus(request):
    return render(request,'contactus/contactus.html')