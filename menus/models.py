from django.db import models
from django_extensions.db.fields import AutoSlugField

from modelcluster.models import ClusterableModel

from wagtail.admin.panels import FieldPanel, PageChooserPanel


class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
    )
    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.title
    