from django.contrib.auth import get_user_model
from django.views.generic import DetailView


class ProfileTemplateView(DetailView):

    model = get_user_model()
    template_name = "profile.html"
    context_object_name = 'user'
    slug_field = 'username'
