from django.shortcuts import render

# Create your views here.


def test_404(request):
    return render(request, 'test_404.html')
