from django.forms import ModelForm

from lepcismagna.models import Inscription

# Form handling the creation of an inscription entry
class InscriptionEntryForm(ModelForm):
    class Meta:
        model = Inscription
        fields = ['inscription_id', 'title', 'description', 'text', 'letters', 'date', 'findspot_desc', 'original_location', 'last_recorded_location', 'transcription_interpretive', 'transcription_diplomatic', 'transcription_appcrit', 'translation_english', 'commentary', 'bibliography_text']