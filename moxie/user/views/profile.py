from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


class ProfileBaseView(DetailView):
    model = get_user_model()
    context_object_name = 'user'
    slug_field = 'username'


class ProfileTemplateView(ProfileBaseView):

    template_name = "profile.html"


class ProfileDashboardTemplateView(ProfileBaseView):

    template_name = "profile_dashboard.html"


class ProfileUpdateTemplateView(ProfileBaseView):

    template_name = "profile_modify.html"

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(
            get_user_model(),
            username=kwargs.get('slug'),
        )

        if not user == self.request.user:
            return redirect(reverse('home'))

        user.alias = request.POST.get('alias', user.alias)
        user.email = request.POST.get('email', user.email)
        user.phonenumber = request.POST.get('phone', user.phonenumber)
        user.is_phonenumber_verified = False
        user.save()

        messages.add_message(
            request,
            messages.SUCCESS,
            '프로필 수정이 완료되었습니다',
            extra_tags='success'
        )

        return redirect(
                reverse(
                    'profile-dashboard',
                    kwargs={
                        'slug': user.username,
                    }
                )
        )
