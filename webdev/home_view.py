from django.http import HttpResponse


def home(requst):
    return HttpResponse('Puritoka')
