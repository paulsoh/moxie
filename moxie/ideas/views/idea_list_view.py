from django.views.generic import ListView

from ideas.models import Idea, Category


class IdeaListView(ListView):

    model = Idea
    template_name = "idea_list_view.html"
    context_object_name = 'ideas'

    def get_context_data(self, **kwargs):
        context = super(IdeaListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
