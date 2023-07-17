from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

apps_rus_dict = {
    'movieman': 'Киноман',
}

def index(request):
    all_apps = settings.INSTALLED_APPS
    user_apps = []
    for app in all_apps:
        if not app.startswith('django') and not app.startswith('smarty'):
            user_apps.append(app)
    data = {
        'apps': user_apps,
        'apps_rus_dict': apps_rus_dict,
    }
    return render(request, 'smarty/index.html', data)