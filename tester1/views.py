from django.shortcuts import render
from tester1.models import employee


def data(request):
    emp=employee.objects.all()
    return render(request,'index.html',{'emp':emp})
