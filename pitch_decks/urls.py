from django.urls import path

from .views import HomePageView, CreatePitchDeckView, DeletePitchDeckView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload_deck/', CreatePitchDeckView.as_view(), name='add_pitch_deck'),
    path('<pk>/delete/', DeletePitchDeckView.as_view()),
]