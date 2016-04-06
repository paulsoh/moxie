from django.views.generic.edit import CreateView

from ideas.models import Idea
from ideas.forms import PostIdeaForm


class IdeaCreateView(CreateView):

    model = Idea
    template_name = "idea_create_view.html"
    form_class = PostIdeaForm
