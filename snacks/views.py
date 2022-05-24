from django.views.generic import ListView
from .models import thing


class SnacksListView(ListView):

    template_name = 'snacks.html'
    model = Snacks
