from django.shortcuts import render

# Create your views here.
def address(request):
    return render(request, 'pages/address.html')