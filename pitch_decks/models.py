from django.db import models


class PitchDeck(models.Model):
    title = models.CharField(max_length=64)
    presentation_file = models.FileField(upload_to='decks/')

    def __str__(self):
        return self.title


class DeckImage(models.Model):
    pitch_deck = models.ForeignKey(PitchDeck, on_delete=models.CASCADE, related_name="deck_images")
    title = models.CharField(max_length=64)
    slide = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
