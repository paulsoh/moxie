from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


def signout(request):
    logout(request)
    return redirect(reverse('home'))
