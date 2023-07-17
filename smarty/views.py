from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def index(request):
    all_apps = settings.INSTALLED_APPS
    user_apps = []
    for app in all_apps:
        if not app.startswith('django'):
            user_apps.append(app)
    data = {
        'apps': user_apps,
    }
    return render(request, 'smarty/index.html', data)