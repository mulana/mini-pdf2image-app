from django.urls import path

from .views import HomePageView, CreatePitchDeckView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload_deck/', CreatePitchDeckView.as_view(), name='add_pitch_deck')

]