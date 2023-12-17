import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.urls import reverse

from .models import UserDossier, Inscription, Bibliography, EpigraphicReference, Category, Abbreviation, AgeAtDeath, DivineSacredBeing, EmperorImperialFamily, Erasure, Findspot, Fragment, Organization, Person, PersonalName, PlaceName, Symbol, Word
from .forms import InscriptionEntryForm, InscriptionSearchForm


def index(request):
    return render(request, "lepcismagna/index.html")
    
# User account handling
def login_view(request):
    if request.method == 'POST':
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "lepcismagna/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "lepcismagna/login.html")
       
def logout_view(request):
    # Render page indicating that user has logged out
    logout(request)
    return render(request, "lepcismagna/logout.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "lepcismagna/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "lepcismagna/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "lepcismagna/register.html")
    
# Logged-in user functionality handling
@login_required
def create_entry(request):
    # Handle the creation of a new inscription entry
    if request.method == 'POST':
        form = InscriptionEntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.entry_creator = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse("inscriptions"))
        else:
            print(form.errors)
    else:
        form = InscriptionEntryForm()
    return render(request, 'lepcismagna/create_entry.html', {'form': form})

@login_required
def dossier(request):
    # Retrieve the user's dossier and display on the dossier page
    user_dossier, created = UserDossier.objects.get_or_create(user=request.user)
    dossier_inscriptions = user_dossier.dossier.all()

    paginator = Paginator(dossier_inscriptions, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "lepcismagna/dossier.html", {
        "page_obj": page_obj,
    })

@login_required
def toggle_dossier(request, inscription_id):
    if request.method == 'POST':
        # Add or remove inscription from dossier
        inscription = get_object_or_404(Inscription, inscription_id=inscription_id)
        user_dossier, created = UserDossier.objects.get_or_create(user=request.user)

        is_in_dossier = inscription in user_dossier.dossier.all()

        if is_in_dossier:
            user_dossier.dossier.remove(inscription)
        else:
            user_dossier.dossier.add(inscription)

    # If the request is not a POST request, redirect to the inscription detail page
    return HttpResponseRedirect(reverse('inscription_detail', args=[inscription_id]))

# Inscription handling
def inscriptions(request):
    # Retrieve inscription entries, display and paginate them (10 inscriptions per page)
    inscriptions = Inscription.objects.all()
    paginator = Paginator(inscriptions, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "lepcismagna/inscriptions.html", {
        "page_obj": page_obj,
    })

def inscription_detail_view(request, inscription_id):
    # Display the details of an inscription
    inscription = get_object_or_404(Inscription, inscription_id=inscription_id)

    # Check if the user is authenticated
    if request.user and request.user.is_authenticated:
        # Ensure that we have a concrete user object
        user = request.user

        # Check if the inscription is in the user's dossier
        user_dossier, created = UserDossier.objects.get_or_create(user=user)
        is_in_dossier = inscription in user_dossier.dossier.all()

    else:
        # If user is not authenticated, set user_dossier and is_in_dossier to None
        user_dossier = None
        is_in_dossier = None

    # Get the previous and next inscription IDs
    all_inscriptions = Inscription.objects.all().order_by('inscription_id')
    all_inscriptions_list = list(all_inscriptions)  # Convert to list
    current_index = all_inscriptions_list.index(inscription)

    previous_id = None
    next_id = None

    if current_index > 0:
        previous_id = all_inscriptions_list[current_index - 1].inscription_id

    if current_index < len(all_inscriptions_list) - 1:
        next_id = all_inscriptions_list[current_index + 1].inscription_id

    return render(request, 'lepcismagna/inscription_detail.html', {
        'inscription': inscription,
        'is_in_dossier': is_in_dossier,
        'previous_id': previous_id,
        'next_id': next_id,
    })

# Category handling
def categories(request):
    # Retrieve all categories and display on categories page
    categories = Category.objects.all()
    return render(request, "lepcismagna/categories.html", {"categories": categories})

def category_view(request, category_name):
    # Get the category object by name or handle error if not found
    category = get_object_or_404(Category, name=category_name)

    # Filter inscriptions based on the selected category and display on category page
    category_inscriptions = Inscription.objects.filter(
        category=category)
    
    paginator = Paginator(category_inscriptions, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "lepcismagna/category_view.html", {
        "page_obj": page_obj,
        'category_name': category_name,
    })  

# Bibliography handling
def bibliography(request):
    bibliography_entries = Bibliography.objects.all()
    epigraphic_references = EpigraphicReference.objects.all()
    return render(request, "lepcismagna/bibliography.html", {
        "bibliography_entries": bibliography_entries,
        "epigraphic_references": epigraphic_references,
        })

# Search handling
def inscription_search(request):
    form = InscriptionSearchForm(request.GET)
    inscriptions = Inscription.objects.all()

    if form.is_valid():
        search_terms = form.cleaned_data.get('search_terms')
        findspot = form.cleaned_data.get('findspot')
        repository = form.cleaned_data.get('repository')
        material = form.cleaned_data.get('material')
        technique = form.cleaned_data.get('technique')
        object_type = form.cleaned_data.get('object_type')
        category = form.cleaned_data.get('category')
        language = form.cleaned_data.get('language')

        # Filter query based on provided search terms
        if search_terms:
            # Remove <br> from the search terms
            search_terms = re.sub(r'<br\s*/*>', '', search_terms, flags=re.IGNORECASE)
            inscriptions = inscriptions.filter(
                Q(title__icontains=search_terms) |
                Q(transcription_interpretive__icontains=search_terms) | 
                Q(translation_english__icontains=search_terms)
            )

        if findspot:
            inscriptions = inscriptions.filter(findspots=findspot)
        
        if repository:
            inscriptions = inscriptions.filter(repositories=repository)

        if material:
            inscriptions = inscriptions.filter(materials=material)

        if technique:
            inscriptions = inscriptions.filter(techniques=technique)

        if object_type:
            inscriptions = inscriptions.filter(object_types=object_type)

        if category:
            inscriptions = inscriptions.filter(categories=category)

        if language:
            inscriptions = inscriptions.filter(languages=language)
    
    return render(request, "lepcismagna/inscription_search.html", {'form': form, 'inscriptions': inscriptions})

# Epigraphic indices handling
def abbreviations(request):
    abbreviations = Abbreviation.objects.prefetch_related('inscriptions')
    return render(request, "lepcismagna/abbreviations.html", {"abbreviations": abbreviations})

def ages_at_death(request):
    ages_at_death = AgeAtDeath.objects.all()
    return render(request, "lepcismagna/ages_at_death.html", {"ages_at_death": ages_at_death})

def divine_sacred_beings(request):
    divine_sacred_beings = DivineSacredBeing.objects.all()
    return render(request, "lepcismagna/divine_sacred_beings.html", {"divine_sacred_beings": divine_sacred_beings})

def emperors_imperial_family(request):
    emperors_imperial_family = EmperorImperialFamily.objects.all()
    return render(request, "lepcismagna/emperors_imperial_family.html", {"emperors_imperial_family": emperors_imperial_family})

def erasures(request):
    erasures = Erasure.objects.all()
    return render(request, "lepcismagna/erasures.html", {"erasures": erasures})

def findspots(request):
    findspots = Findspot.objects.all()
    return render(request, "lepcismagna/findspots.html", {"findspots": findspots})

def fragments(request):
    fragments = Fragment.objects.all()
    return render(request, "lepcismagna/fragments.html", {"fragments": fragments})

def organizations(request):
    organizations = Organization.objects.all()
    return render(request, "lepcismagna/organizations.html", {"organizations": organizations})

def people(request):
    people = Person.objects.all()
    return render(request, "lepcismagna/people.html", {"people": people})

def personal_names(request):
    personal_names = PersonalName.objects.all()
    return render(request, "lepcismagna/personal_names.html", {"personal_names": personal_names})

def place_names(request):
    place_names = PlaceName.objects.all()
    return render(request, "lepcismagna/place_names.html", {"place_names": place_names})

def symbols(request):
    symbols = Symbol.objects.all()
    return render(request, "lepcismagna/symbols.html", {"symbols": symbols})

def words(request):
    words = Word.objects.all()
    return render(request, "lepcismagna/words.html", {"words": words})
