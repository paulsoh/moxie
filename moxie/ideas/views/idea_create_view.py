from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from ideas.models import Idea
from ideas.forms import PostIdeaForm


class IdeaCreateView(LoginRequiredMixin, CreateView):

    model = Idea
    template_name = "idea_create_view.html"
    form_class = PostIdeaForm

    login_url = '/'

    def get_redirect_field_name(self):
        messages.add_message(
            self.request,
            messages.INFO,
            '가입 후 이용해주세요',
            extra_tags="success",
        )
        return super(IdeaCreateView, self).get_redirect_field_name()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IdeaCreateView, self).form_valid(form)
