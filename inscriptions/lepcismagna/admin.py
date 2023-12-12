from django.contrib import admin
from .models import Inscription, Bibliography, InscriptionBibliography, EpigraphicReference, InscriptionReference, Category, Image, Abbreviation, InscriptionAbbreviation, AgeAtDeath, DivineSacredBeing, EmperorImperialFamily, Erasure, Findspot, Fragment, Language, Material, ObjectType, Organization, Person, PersonalName, PlaceName, Repository, Technique, Symbol, Word

# Register your models here.
admin.site.register(Inscription)
admin.site.register(Bibliography)
admin.site.register(InscriptionBibliography)
admin.site.register(EpigraphicReference)
admin.site.register(InscriptionReference)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Abbreviation)
admin.site.register(InscriptionAbbreviation)
admin.site.register(AgeAtDeath)
admin.site.register(DivineSacredBeing)
admin.site.register(EmperorImperialFamily)
admin.site.register(Erasure)
admin.site.register(Findspot)
admin.site.register(Fragment)
admin.site.register(Language)
admin.site.register(Material)
admin.site.register(ObjectType)
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(PersonalName)
admin.site.register(PlaceName)
admin.site.register(Repository)
admin.site.register(Symbol)
admin.site.register(Technique)
admin.site.register(Word)
