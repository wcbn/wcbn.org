from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'homepage.html'
    title = 'Homepage'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context
