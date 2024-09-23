from allauth.socialaccount.providers.netiq_provider.provider import NetIQProvider
from allauth.socialaccount.providers.oauth2_provider.urls import default_urlpatterns


urlpatterns = default_urlpatterns(NetIQProvider)
