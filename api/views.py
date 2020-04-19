from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return render(
        request,
        'index.html'
    )


def who_am_i(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    language = request.META.get('HTTP_ACCEPT_LANGUAGE')
    user_agent = request.META.get('HTTP_USER_AGENT')
    return JsonResponse({
        'ipaddress': ip,
        'language': language,
        'software': user_agent
    })
