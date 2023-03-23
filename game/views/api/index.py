from django.shortcuts import render

def index(request):
    return render(request=request,template_name="index.html")

def test(request):
    return render(request=request,
    template_name="test.html")