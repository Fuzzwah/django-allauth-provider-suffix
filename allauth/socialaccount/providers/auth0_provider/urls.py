from allauth.socialaccount.providers.auth0_provider.provider import Auth0Provider
from allauth.socialaccount.providers.oauth2_provider.urls import default_urlpatterns


urlpatterns = default_urlpatterns(Auth0Provider)
