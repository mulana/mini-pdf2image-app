from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import PitchDeckForm
from .models import PitchDeck


# We should probably have some pagination here.
class HomePageView(ListView):
    model = PitchDeck
    template_name = 'home.html'


class CreatePitchDeckView(CreateView):
    model = PitchDeck
    form_class = PitchDeckForm
    template_name = 'upload_deck.html'
    success_url = reverse_lazy('home')


class DeletePitchDeckView(DeleteView):
    model = PitchDeck

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return JsonResponse({})
