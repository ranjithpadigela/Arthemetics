from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'input.html')

class Add(View):
    def get(self,request):
        x = request.GET['t1']
        y = request.GET['t2']
        op = request.GET['operation']
        if op == 'add':
            i = int(x)
            j = int(y)
            k = i+j
            res = HttpResponse("The Sum is: " + str(k))
        elif op == 'sub':
            i = int(x)
            j = int(y)
            k = i-j
            res = HttpResponse("The Subtration is: " + str(k))
        elif op == 'mul':
            i = int(x)
            j = int(y)
            k = i*j
            res = HttpResponse("The Multiplication is: " + str(k))
        else:
            i = int(x)
            j = int(y)
            k = i/j
            res =HttpResponse("The Division is: "+str(k))
        return res