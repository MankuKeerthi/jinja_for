from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'Name':'keerthi','age':'21'}
    return render(request,'forloop.html',d)