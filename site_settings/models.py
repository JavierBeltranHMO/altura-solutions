from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    facebook = models.URLField(blank=True, help_text="Enter your Facebook URL")
    x = models.URLField(blank=True, help_text="Enter your X URL")
    youtube = models.URLField(blank=True, help_text="Enter your Youtube URL")
    instagram = models.URLField(blank=True, help_text="Enter your Instagram URL")

    panels = [
        FieldPanel("facebook"),
        FieldPanel("x"),
        FieldPanel("youtube"),
        FieldPanel("instagram"),
    ]
