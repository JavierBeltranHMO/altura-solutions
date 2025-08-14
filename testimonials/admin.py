from wagtail_modeladmin.options import ModelAdmin, modeladmin_register

from .models import Testimonial


@modeladmin_register
class TestimonialAdmin(ModelAdmin):
    model = Testimonial
    menu_label = "Testimonials"
    menu_icon = "placeholder"
    menu_order = 86
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("quote", "author")
    search_fields = ("quote", "author")
