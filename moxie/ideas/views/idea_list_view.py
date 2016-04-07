from django.views.generic import ListView

from ideas.models import Idea


class IdeaListView(ListView):

    model = Idea
    template_name = "idea_list_view.html"
    context_object_name = 'ideas'
