from django.views.generic import DetailView

from django.contrib.auth.models import User


class ProfileTemplateView(DetailView):

    model = User
    template_name = "profile.html"
    context_object_name = 'user'
    slug_field = 'username'
