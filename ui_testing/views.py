from django.shortcuts import render

# Create your views here.


def test_404(request):
    range_list = [
        f'ui_testing/sandbox/img/demos/mi{i}.jpg' for i in range(1, 35)]
    context = {
        'range_list': range_list
    }
    return render(request, 'resume.html', context)
