from django.views.generic.edit import UpdateView

from ideas.models import Idea
from ideas.forms import UpdateIdeaForm


class IdeaUpdateView(UpdateView):

    model = Idea
    template_name = "idea_update_view.html"
    form_class = UpdateIdeaForm
    slug_field = 'custom_slug'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IdeaUpdateView, self).form_valid(form)
