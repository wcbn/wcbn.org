import requests
from django.views.generic import ListView
from wcbn_cms.models import Article
from django.conf import settings

def get_on_air():
    url = f'{settings.READBACK_URL}/playlist.json'
    resp = requests.get(url)
    return resp.json()


class IndexView(ListView):
    template_name = 'layouts/main_with_aside.html'
    model = Article
    ordering = ['-published_at']

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Homepage'
        context['STUDIO_LINE'] = settings.STUDIO_LINE
        context['RESOURCE_LINKS'] = settings.RESOURCE_LINKS
        context['on_air'] = get_on_air()['on_air'] if 'prod' in settings.DJANGO_SETTINGS_MODULE else {}
        context['main'] = "articles/list.html"
        context['aside'] = "homepage/aside.html"
        return context
