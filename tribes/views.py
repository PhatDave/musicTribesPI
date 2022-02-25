from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    html = 'tribes/index.html'
    return render(request, html, context)
