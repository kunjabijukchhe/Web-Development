from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def other(request):
    return render(request,'other.html')

def main(request):
    return render(request,'main.html')
