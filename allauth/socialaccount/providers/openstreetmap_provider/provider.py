from allauth.socialaccount.providers.base_provider import ProviderAccount
from allauth.socialaccount.providers.oauth_provider.provider import OAuthProvider
from allauth.socialaccount.providers.openstreetmap_provider.views import (
    OpenStreetMapOAuthAdapter,
)


class OpenStreetMapAccount(ProviderAccount):
    def get_profile_url(self):
        return (
            "https://www.openstreetmap.org/user/"
            + self.account.extra_data["display_name"]
        )

    def get_avatar_url(self):
        return self.account.extra_data.get("avatar")

    def get_username(self):
        return self.account.extra_data["display_name"]


class OpenStreetMapProvider(OAuthProvider):
    id = "openstreetmap"
    name = "OpenStreetMap"
    account_class = OpenStreetMapAccount
    oauth_adapter_class = OpenStreetMapOAuthAdapter

    def extract_uid(self, data):
        return data["id"]

    def extract_common_fields(self, data):
        return dict(username=data["display_name"])


provider_classes = [OpenStreetMapProvider]
