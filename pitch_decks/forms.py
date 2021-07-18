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
        # TODO: This is not the right place to do this as we should do this during validation so we can return
        # a meaningful message to the user
        pitch_deck = None
        try:
            pitch_deck = super().save(commit)
            # Remove leading '/' to get relative path
            path = pitch_deck.presentation_file.url.lstrip('/')
            images = convert_from_path(path)
            cnt = 0
            for img in images:
                deck_image = DeckImage()

                # A better naming scheme can probably be applied
                deck_image.title = f"slide-{cnt}"
                deck_image.pitch_deck = pitch_deck

                # We will use in memory IO
                # Taken from: https://stackoverflow.com/questions/3723220/how-do-you-convert-a-pil-image-to-a-django-file
                img_io = BytesIO()
                # Save parsed image to in memory IO
                img.save(img_io, format='JPEG')

                # Get the file to be forwarded as slide to model and then save
                img_file = ContentFile(img_io.getvalue())
                deck_image.slide.save(f"{cnt}", img_file, True)

                cnt += 1

            return pitch_deck
        except Exception as e:
            if pitch_deck is not None:
                # if an error occurred remove pitch deck and slides to not clutter the db
                pitch_deck.delete()
                raise ValueError("Error parsing slides: ", e)


