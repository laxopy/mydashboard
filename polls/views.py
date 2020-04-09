from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're right here, at the polls index.")
