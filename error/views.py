from django.shortcuts import render


# Create your views here.
def page_not_found(request):
    return render(request, '404.html')


def service_error(request):
    return render(request, '500.html')

def bad_request(request):
    return render(request, '400.html')
