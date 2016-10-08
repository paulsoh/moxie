from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View


from user.utils import send_sms


class UserVerifyPhoneView(View):

    def get(self, request, **kwargs):
        user = get_object_or_404(
            get_user_model(),
            phonenumber_verification_token=kwargs['slug']
        )

        user.is_phonenumber_verified = True
        user.save()

        messages.add_message(
            request,
            messages.INFO,
            '휴대폰 인증이 완료되었습니다.',
            extra_tags="success",
        )

        return redirect(reverse('home'))

    def post(self, request, **kwargs):

        if not request.user.is_authenticated():
            messages.add_message(
                request,
                messages.INFO,
                '로그인 후에 연락처 인증이 가능합니다.',
                extra_tags="success",
            )
            return redirect(reverse('home'))

        user = request.user
        phonenumber = request.POST.get('phone', '01023024321')
        user.phonenumber_verification_token = user.generate_and_get_verification_token()
        user.phonenumber = phonenumber
        user.save()

        send_sms(phonenumber, user.phonenumber_verification_token)

        messages.add_message(
            request,
            messages.INFO,
            '연락처로 발송된 인증URL로 접속하시면 인증이 완료됩니다',
            extra_tags="success",
        )

        return redirect(
                reverse(
                    'profile-dashboard',
                    kwargs={
                        'slug': user.username,
                    }
                )
        )
