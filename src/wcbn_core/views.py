import requests
import os
from django.views.generic import ListView
from wcbn_cms.models import Article
from django.conf import settings

def get_on_air():
    url = f'{settings.READBACK_URL}/playlist.json'
    resp = requests.get(url)
    return resp.json()


class IndexView(ListView):
    template_name = 'homepage/homepage.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Homepage'
        context['STUDIO_LINE'] = settings.STUDIO_LINE
        context['RESOURCE_LINKS'] = settings.RESOURCE_LINKS
        context['on_air'] = get_on_air()['on_air'] if 'prod' in os.environ.get("DJANGO_SETTINGS_MODULE") else {}
        return context
