from django.views.generic.edit import FormView

from ideas.models import Idea
from ideas.forms import PostIdeaForm


class IdeaCreateView(FormView):

    model = Idea
    form_class = PostIdeaForm
    template_name = "idea_create_view.html"
