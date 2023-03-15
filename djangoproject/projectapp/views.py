from django.shortcuts import render
from . models import Place
from . models import Persons
# Create your views here.
from django.http import HttpResponse


# def demo1(request):
#     # name = "India"
#     return render(request, "index1.html")

# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x+y
#     return render(request, "result.html", {'result': res})


#
def demo(request):
    obj = Place.objects.all()
    obj1 = Persons.objects.all()
    return render(request, "index.html", {'result': obj,'result1':obj1})

# def demos(request):
#     obj1 = Persons.objects.all()
#     return render(request, "index.html", {'result1': obj1})
# #
# # def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("Hello World")
