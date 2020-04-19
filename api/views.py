from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return render(
        request,
        'index.html'
    )


def who_am_i(request):
    ipaddress = request.META.get('HTTP_HOST')
    language = request.META.get('HTTP_ACCEPT_LANGUAGE')
    user_agent = request.META.get('HTTP_USER_AGENT')
    return JsonResponse({
        'ipaddress': ipaddress,
        'language': language,
        'software': user_agent
    })
