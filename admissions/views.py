from django.shortcuts import render

def admissions(request):
    return render(request,'admissions/admissions.html')