from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel


class ServiceListingPage(Page):
    parent_page_types = ["home.HomePage"]
    max_count = 1
    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["services"] = ServicePage.objects.live().public()
        return context


class ServicePage(Page):
    parent_page_types = ["services.ServiceListingPage"]
    subpage_types = []
    description = models.TextField(
        blank=True,
        max_length=500,
    )
    internal_page = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        related_name="+",
        help_text="Select an interanl Wagtail page",
        on_delete=models.SET_NULL,
    )
    external_page = models.URLField(
        blank=True,
    )
    button_text = models.CharField(blank=True, max_length=50)
    service_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text="Image used in Service Listing Page and will be cropped to 570x370 pixels",
        related_name="+",
    )
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        PageChooserPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("button_text"),
        FieldPanel("service_image"),
    ]

    def clean(self):
        super().clean()
        v_error_message = "Please select an internal page OR enter an external URL"
        if (self.internal_page and self.external_page) or (
            not self.internal_page and not self.external_page
        ):
            raise ValidationError(
                {
                    "internal_page": ValidationError(v_error_message),
                    "external_page": ValidationError(v_error_message),
                }
            )

    def get_context(self, request):
        context = super().get_context(request)
        context["STRIPE_PUBLISHABLE_KEY"] = settings.STRIPE_PUBLISHABLE_KEY
        return context
