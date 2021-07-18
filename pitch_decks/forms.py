from django import forms
from .models import PitchDeck, DeckImage
from io import BytesIO
from pdf2image import convert_from_path
from django.core.files.base import ContentFile


class PitchDeckForm(forms.ModelForm):

    class Meta:
        model = PitchDeck
        fields = ['title', 'presentation_file']

    def save(self, commit=True):
        pitch_deck = super().save(commit)
        return pitch_deck
