from django.shortcuts import render

# Create your views here.
def openIndex(request):
    return render(request,'index.html')
