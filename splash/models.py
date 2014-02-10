"""
Models for the splash screen application
"""
from django.db import models

from config_models.models import ConfigurationModel


class SplashConfig(ConfigurationModel):
    """
    Configuration for the splash django app
    """
    cookie_name = models.TextField(
        default='edx_splash_screen',
        help_text="The name of the cookie to check when assessing if the user needs to be redirected"
    )
    cookie_allowed_values = models.TextField(
        default='seen',
        help_text="Comma-separated list of values accepted as cookie values to prevent the redirect"
    )
    unaffected_usernames = models.TextField(
        default='',
        blank=True,
        help_text="Comma-separated list of users which should never be redirected (usernames)"
    )
    redirect_url = models.URLField(
        default='http://edx.org',
        help_text="The URL the users should be redirected to when they don't have the right cookie"
    )

    @property
    def cookie_allowed_values_list(self):
        """
        `cookie_allowed_values` as a list of string values
        """
        if not self.cookie_allowed_values.strip():  # pylint: disable=no-member
            return []

        return [val.strip() for val in self.cookie_allowed_values.split(',')]  # pylint: disable=no-member
    
    @property
    def unaffected_usernames_list(self):
        """
        `unaffected_usernames` as a list of username values
        """
        if not self.unaffected_usernames.strip():  # pylint: disable=no-member
            return []

        return [name.strip() for name in self.unaffected_usernames.split(',')]  # pylint: disable=no-member
    
    #DarkLangConfig.current().released_languages_list