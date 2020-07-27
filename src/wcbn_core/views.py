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
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['title'] = 'Homepage'
        ctx['STUDIO_LINE'] = settings.STUDIO_LINE
        ctx['RESOURCE_LINKS'] = settings.RESOURCE_LINKS
        ctx['on_air'] = get_on_air()['on_air'] if 'prod' in settings.DJANGO_SETTINGS_MODULE else {}
        ctx['main'] = "articles/list.html"
        ctx['aside'] = "homepage/aside.html"
        ctx['IOS_URL'] = settings.IOS_URL
        ctx['ANDROID_URL'] = settings.ANDROID_URL
        return ctx
