from django.db import models
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField


@register_setting
class ContactSettings(BaseSiteSetting):
    contact = RichTextField(
        blank=True,
        null=True,
        features=["link"],
    )
    panels = [FieldPanel("contact")]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_contact_settings")
        cache.delete(key)
        return super().save(*args, **kwargs)


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
    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_social_settings")
        cache.delete(key)
        return super().save(*args, **kwargs)