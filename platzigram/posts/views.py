from django.shortcuts import render
from django.http import HttpResponse

# Utilities
from datetime import datetime


# Create your views here.

posts = [
    {
    'name': 'Vía Lactea',
    'user': 'irg',
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
    'name': 'Auditorio',
    'user': 'aam',
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
    'name': 'Paz y libertad',
    'user': 'vgr',
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]

def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src={picture} /></figure>
        """.format(**post)
        )
    return HttpResponse('<br>'.join(content))
