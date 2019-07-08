from django.http import HttpResponse

from datetime import datetime

def hello_world(request):
    return HttpResponse("Hola, mundo!<br>{now}".format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))