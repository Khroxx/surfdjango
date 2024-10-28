from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from surfdjango.corporations.models import Corporation


class CorporationCreateView(SuccessMessageMixin, CreateView):
    model = Corporation
    fields = ["name", "address", "url", "user"]
    template_name = "corporations/corporations_create.html"
    success_message = _("Corporation successfully created")

    def get_success_url(self):
        return reverse_lazy("corporations:list")


create_corp_view = CorporationCreateView.as_view()


class CorportaionUpdateView(SuccessMessageMixin, UpdateView):
    model = Corporation
    fields = ["name", "address", "url", "user"]
    template_name = "corporations/corporations_update.html"
    success_message = _("Corporation successfully updated")

    def get_success_url(self):
        return reverse_lazy("corporations:list")


update_corp_view = CorportaionUpdateView.as_view()


class CorporationDeleteView(SuccessMessageMixin, DeleteView):
    model = Corporation
    fields = ["name", "address", "url", "user"]
    template_name = "corporations/corporations_delete.html"
    success_message = _("Corporation successfully updated")

    def get_success_url(self):
        return reverse_lazy("corporations:list")


delete_corp_view = CorporationDeleteView.as_view()
