"""URLs for Patreon Provider"""

from allauth.socialaccount.providers.oauth2_provider.urls import default_urlpatterns

from .provider import VimeoOAuth2Provider


urlpatterns = default_urlpatterns(VimeoOAuth2Provider)
