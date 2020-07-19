from django.shortcuts import render

from . import util


def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)

    if entry is not None:
        return render(request, 'encyclopedia/entry.html')
    else:
        # Render an error page
        return render(request, 'encyclopedia/error.html', {
            'error_code': 404,
            'error_message': 'Page Not Found'
        })
