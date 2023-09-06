# https://docs.djangoproject.com/en/4.2/ref/class-based-views/

from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy




from .models import Email


class EmailListView(ListView):
    model = Email
    paginate_by = 10  # if pagination is desired
    template_name = "generic/list.html" # default location `polls/email_list.html`

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EmailDetailView(DetailView):
    model = Email
    template_name = "generic/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time"] = timezone.now()
        return context


class EmailUpdateView(UpdateView):
    model = Email
    fields = '__all__'
    template_name = "generic/edit.html"
    success_url = reverse_lazy("polls:generic-email-list")


class EmailCreateView(CreateView):
    model = Email
    fields = "__all__"
    template_name = "generic/create.html"
    success_url = reverse_lazy("polls:generic-email-list")