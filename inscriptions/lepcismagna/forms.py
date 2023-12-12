from django import forms

from lepcismagna.models import Inscription, Findspot, Repository, Material, Technique, ObjectType, Category, Language

# Form handling the creation of an inscription entry
class InscriptionEntryForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['inscription_id', 'title', 'description', 'text', 'letters', 'date', 'findspot_desc', 'original_location', 'last_recorded_location', 'transcription_interpretive', 'transcription_diplomatic', 'transcription_appcrit', 'translation_english', 'commentary', 'bibliography_text']

class InscriptionSearchForm(forms.Form):
    search_terms = forms.CharField(label='Search Terms', required=False)
    findspot = forms.ModelChoiceField(queryset=Findspot.objects.all(), required=False, label='Findspot')
    repository = forms.ModelChoiceField(queryset=Repository.objects.all(), required=False, label='Repository')
    material = forms.ModelChoiceField(queryset=Material.objects.all(), required=False, label='Material')
    technique = forms.ModelChoiceField(queryset=Technique.objects.all(), required=False, label='Technique')
    object_type = forms.ModelChoiceField(queryset=ObjectType.objects.all(), required=False, label='Object Type')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Category')
    language = forms.ModelChoiceField(queryset=Language.objects.all(), required=False, label='Language')