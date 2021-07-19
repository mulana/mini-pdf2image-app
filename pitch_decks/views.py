from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import PitchDeckForm
from .models import PitchDeck
from django.contrib.auth.mixins import LoginRequiredMixin


# We should probably have some pagination here.
class HomePageView(ListView):
    model = PitchDeck
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(HomePageView, self).get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            context['decks'] = []
            return context
        # Create any data and add it to the context
        context['decks'] = PitchDeck.objects.filter(user=self.request.user)
        return context


class CreatePitchDeckView(LoginRequiredMixin, CreateView):
    model = PitchDeck
    form_class = PitchDeckForm
    template_name = 'upload_deck.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeletePitchDeckView(LoginRequiredMixin, DeleteView):
    model = PitchDeck

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return JsonResponse({})
