from django.views.generic import DetailView

from ideas.models import Idea


class IdeaDetailView(DetailView):

    model = Idea
    template_name = "idea_detail_view.html"
    context_object_name = 'idea'
