from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from ideas.models import Idea


class IdeaAdminTemplateView(UserPassesTestMixin, DetailView):

    model = Idea
    template_name = "idea_admin.html"
    context_object_name = 'idea'
    slug_field = 'custom_slug'

    login_url = '/'
    raise_exception = False

    def test_func(self):
        if self.request.user == self.get_object().user:
            return True
        else:
            messages.add_message(self.request, messages.WARNING, '아이디어 작성자만 접근할 수 있습니다')
            return False
