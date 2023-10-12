from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Client


class IndexView(generic.ListView):
    template_name = "clients/index.html"
    context_object_name = "all_clients"
    
    def get_queryset(self):
        return Client.objects.order_by("-first_name")

class DetailsView(generic.ListView):
    template_name = "clients/details.html"
    context_object_name = "all_clients"
    
    def get_queryset(self):
        return Client.objects.order_by("-first_name")

class SignUpView(generic.ListView):
    model = Client
    template_name = "clients/sign_up.html"