from django.views.generic import TemplateView

from ideas.models import Idea


class HomeTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['ideas'] = Idea.objects.all()[:6]
        return context
