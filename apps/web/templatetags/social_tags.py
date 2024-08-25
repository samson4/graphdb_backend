from allauth.socialaccount.models import SocialApp
from django import template
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_socialapps(context):
    """
    Returns a list of social authentication apps.

    Usage: `{% get_socialapps as socialapps %}`.

    Then within the template context, `socialapps` will hold
    a list of social apps configured for the current site.
    """
    providers = list(settings.SOCIALACCOUNT_PROVIDERS)
    apps = SocialApp.objects.filter(sites=get_current_site(context["request"])).all()
    for app in apps:
        if app.provider not in providers:
            providers.remove(app.provider)
    # sort the providers according to the order in settings
    return list(sorted(apps, key=lambda a: providers.index(a.provider)))
