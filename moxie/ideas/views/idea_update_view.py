from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from ideas.models import Idea
from ideas.forms import UpdateIdeaForm


class IdeaUpdateView(LoginRequiredMixin, UpdateView):

    model = Idea
    template_name = "idea_update_view.html"
    form_class = UpdateIdeaForm
    slug_field = 'custom_slug'

    login_url = '/'

    def get_redirect_field_name(self):
        messages.add_message(
            self.request,
            messages.INFO,
            '가입 후 이용해주세요',
            extra_tags="success",
        )
        return super(IdeaUpdateView, self).get_redirect_field_name()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IdeaUpdateView, self).form_valid(form)
