from django.shortcuts import render

from social.pipeline.partial import partial


@partial
def get_user_description(backend, details, response, request, user, is_new=False, *args, **kwargs):
    if backend.name == 'facebook' and is_new:
        data = backend.strategy.request_data()
        profile_url = "http://graph.facebook.com/{fb_id}/picture?type=large".format(
            fb_id=response.get('id', '1693581180899208')
        )

        if data.get('phone') is None:
            return render(
                backend.strategy.request,
                'user_extra_data_form.html',
                context={
                    'facebook_user': details,
                    'profile_url': profile_url,
                },
            )
        else:
            return {
                'phone': data.get('phone', ''),
                'alias': data.get('alias', ''),
                'email': data.get('email', ''),
            }


def save_profile(backend, user, response, is_new, *args, **kwargs):
    if backend.name == 'facebook':
        user.alias = kwargs.get('alias')
        user.email = kwargs.get('email')
        user.phonenumber = kwargs.get('phone')
        user.save()
