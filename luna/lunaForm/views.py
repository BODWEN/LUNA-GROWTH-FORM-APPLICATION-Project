from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def applicant(request):
    return render(request, 'applicant.html')

def guarantor(request):
    return render(request, 'guarantor.html')