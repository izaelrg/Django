# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime


# Create your views here.

posts = [
    {
    'title': 'Vía Lactea',
    'user':{
        'name': 'irg',
        'picture': 'https://picsum.photos/60/60/?image=1005',
    }, 
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/200/200/?image=1036',
    },
    {
    'title': 'Auditorio',
    'user': {
        'name': 'aam',
        'picture': 'https://picsum.photos/60/60/?image=883',
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/200/200/?image=903',
    },
    {
    'title': 'Paz y libertad',
    'user': {
        'name': 'cgr',
        'photo': 'https://picsum.photos/60/60/?image=1027',
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/200/200/?image=1076',
    }
]

@login_required
def list_posts(request):
    return render(request, 'posts/feed.html', {'posts': posts})
