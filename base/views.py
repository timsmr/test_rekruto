from django.shortcuts import render

def index(request):
    params = {
        'name': request.GET.get('name', '').capitalize(),
        'message': request.GET.get('message', '').capitalize()
    }
    return render(request, 'base/index.html', params)