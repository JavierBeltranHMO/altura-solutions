from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet, ViewSetGroup

from .models import Menu
from .forms import MenuForm


class MenuViewSet(ModelViewSet):
    model = Menu
    icon = "list-ul"
    form_class = MenuForm

    list_display = ("title", "slug")
    form_fields = ["title", "slug"]
    search_fields = ["title"]


class MenuGroup(ViewSetGroup):
    menu_label = "Navigation"
    menu_icon = "site"
    menu_order = 200
    items = [MenuViewSet]


@hooks.register("register_admin_viewset")
def register_menu_viewsets():
    return MenuGroup()
