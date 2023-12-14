from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Model for user handling
class UserDossier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dossier = models.ManyToManyField("Inscription", blank=True, related_name="dossiers")

    def __str__(self):
        return self.user

 # Primary model for inscriptions   
class Inscription(models.Model):
    entry_creation_time = models.DateTimeField(auto_now_add=True)
    entry_creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_validated = models.BooleanField(default=False)
    inscription_id = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    materials = models.ManyToManyField('Material', blank=True, related_name='materials')
    object_types = models.ManyToManyField('ObjectType', blank=True, related_name='object_types')
    text = models.TextField(blank=True)
    techniques = models.ManyToManyField('Technique', blank=True, related_name='techniques')
    letters = models.TextField(blank=True)
    languages = models.ManyToManyField('Language', blank=True, related_name='languages')
    date = models.CharField(max_length=50)
    findspot_desc = models.TextField(blank=True)
    associated_inscr = models.ManyToManyField('self', blank=True)
    original_location = models.CharField(max_length=255)
    last_recorded_location = models.CharField(max_length=255)
    repositories = models.ManyToManyField('Repository', blank=True, related_name='repositories')
    categories = models.ManyToManyField('Category', blank=True, related_name='categories')
    transcription_interpretive = models.TextField(blank=True)
    transcription_diplomatic = models.TextField(blank=True)
    transcription_appcrit = models.TextField(blank=True)
    translation_english = models.TextField(blank=True)
    commentary = models.TextField(blank=True)
    epigraphic_references = models.ManyToManyField('EpigraphicReference', blank=True, related_name='epigraphic_references')
    bibliography_text = models.TextField(blank=True)
    bibliography_entries = models.ManyToManyField('Bibliography', blank=True, related_name='bibliography_entries')
    images = models.ManyToManyField('Image', blank=True, related_name='images')
    abbreviations = models.ManyToManyField('Abbreviation', blank=True, related_name='abbreviations')
    age_at_death = models.ManyToManyField('AgeAtDeath', blank=True, related_name='age_at_death')
    divine_sacred_beings = models.ManyToManyField('DivineSacredBeing', blank=True, related_name='divine_sacred_beings')
    emperors_imperial_family = models.ManyToManyField('EmperorImperialFamily', blank=True, related_name='emperors_imperial_family')
    erasures = models.ManyToManyField('Erasure', blank=True, related_name='erasures')
    findspots = models.ManyToManyField('Findspot', blank=True, related_name='findspots')
    fragments = models.ManyToManyField('Fragment', blank=True, related_name='fragments')
    organizations = models.ManyToManyField('Organization', blank=True, related_name='organizations')
    people = models.ManyToManyField('Person', blank=True, related_name='people')
    personal_names = models.ManyToManyField('PersonalName', blank=True, related_name='personal_names')
    place_names = models.ManyToManyField('PlaceName', blank=True, related_name='place_names')
    symbols = models.ManyToManyField('Symbol', blank=True, related_name='symbols')
    words = models.ManyToManyField('Word', blank=True, related_name='words')

    def __str__(self):
        return f"{ self.inscription_id } - { self.title }"


# Models for bibliography information handling
class Bibliography(models.Model):

    class Meta:
        verbose_name_plural = 'bibliographies'

    short_title = models.CharField(max_length=50, blank=True)
    entry = models.TextField(blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.short_title
    

class InscriptionBibliography(models.Model):

    class Meta:
        verbose_name_plural = 'inscription bibliographies'

    inscriptions = models.ForeignKey('Inscription', on_delete=models.CASCADE, null=True)
    bibliography = models.ForeignKey('Bibliography', on_delete=models.CASCADE, null=True)
    page_number_references = models.CharField(max_length=50)

class EpigraphicReference(models.Model):
    short_title = models.CharField(max_length=50, blank=True)
    entry = models.TextField(blank=True)
    inscriptions = models.ManyToManyField('Inscription', through='InscriptionReference', blank=True)

    def __str__(self):
        return self.short_title

# Through model connecting Inscription and EpigraphicReference
class InscriptionReference(models.Model):
    inscription = models.ForeignKey('Inscription', on_delete=models.CASCADE, null=True)
    reference = models.ForeignKey('EpigraphicReference', on_delete=models.CASCADE, null=True)
    reference_number = models.CharField(max_length=20, blank=True)


# Model for category handling
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.name
    
# Model for image handling
class Image(models.Model):
    inscription_id = models.ForeignKey('Inscription', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{ self.inscription_id } - { self.caption }"


# Models for index handling
class Abbreviation(models.Model):
    abbreviation = models.CharField(max_length=20, blank=True)
    expansion = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', through='InscriptionAbbreviation', blank=True)
    
    def __str__(self):
        return f"{ self.abbreviation } - { self.expansion }"
    

# Through model for the relationship between Inscription and Abbreviation
class InscriptionAbbreviation(models.Model):
    inscription = models.ForeignKey('Inscription', on_delete=models.CASCADE, null=True)
    abbreviation = models.ForeignKey('Abbreviation', on_delete=models.CASCADE, null=True)
    line_number_reference = models.CharField(max_length=50, blank=True)

class AgeAtDeath(models.Model):

    class Meta:
        verbose_name_plural = 'ages at death'

    age = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.age

class DivineSacredBeing(models.Model):

    class Meta:
        verbose_name_plural = 'divine and sacred beings'

    divine_being = models.CharField(max_length=50, blank=True)
    epithet = models.CharField(max_length=50, blank=True)
    external_resource = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return f"{ self.divine_being } - { self.epithet }"

class EmperorImperialFamily(models.Model):

    class Meta:
        verbose_name_plural = 'emperors and imperial family members'

    person = models.CharField(max_length=50, blank=True)
    regnal_name = models.CharField(max_length=255, blank=True)
    epithet = models.CharField(max_length=255, blank=True)
    life = models.CharField(max_length=25, blank=True)
    reign = models.CharField(max_length=25, blank=True)
    external_resource = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.person

class Erasure(models.Model):
    erased_text = models.TextField(blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.erased_text

class Findspot(models.Model):
    findspots_upper = models.CharField(max_length=255, blank=True)
    findspots_intermediate = models.CharField(max_length=255, blank=True)
    findspots_lower = models.CharField(max_length=255, blank=True)
    gazetteer = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return f"{self.findspots_upper}, {self.findspots_intermediate}, {self.findspots_lower}"

class Fragment(models.Model):
    fragment = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.fragment
    
class Language(models.Model):
    language = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.language
    
class Material(models.Model):
    material = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.material
    
class ObjectType(models.Model):
    object_type = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.object_type

class Organization(models.Model):
    name = models.CharField(max_length=255, blank=True)
    epithets = models.CharField(max_length=255, blank=True)
    external_resource = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return f"{ self.name } - { self.epithets }"

class Person(models.Model):

    class Meta:
        verbose_name_plural = 'people'

    person = models.CharField(max_length=100, blank=True)
    external_resource = models.CharField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.person

class PersonalName(models.Model):
    name = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.name

class PlaceName(models.Model):
    place_name = models.CharField(max_length=100, blank=True)
    attested_form = models.CharField(max_length=100, blank=True)
    toponym_ethnic = models.CharField(max_length=10, blank=True)
    external_resource = models.URLField(max_length=255, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return f"{ self.place_name } - { self.attested_form }"
    
class Repository(models.Model):
    class Meta:
        verbose_name_plural = 'repositories'

    repository = models.CharField(max_length=100, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.repository

class Symbol(models.Model):
    symbol = models.CharField(max_length=20, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.symbol
    
class Technique(models.Model):
    technique = models.CharField(max_length=50, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.technique

class Word(models.Model):
    lemma = models.CharField(max_length=20, blank=True)
    language_code = models.CharField(max_length=2, blank=True)
    inscriptions = models.ManyToManyField('Inscription', blank=True)

    def __str__(self):
        return self.lemma