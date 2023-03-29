from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def ajax_view(request):
    # your code to process the Ajax request
    data = {'message_value': 'Hello, Ajax! just for echeck'}
    return JsonResponse(data)


def index(request):
    return render(request, 'index.html' )