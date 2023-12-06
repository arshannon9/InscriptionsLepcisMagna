from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("create_entry", views.create_entry, name="create_entry"),
    path("dossier", views.dossier, name="dossier"),
    path("toggle_dossier/<str:inscription_id>", views.toggle_dossier, name="toggle_dossier"),
    path("inscriptions", views.inscriptions, name="inscriptions"),
    path("inscriptions/<str:inscription_id>", views.inscription_detail_view, name="inscription_detail"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:category_name>", views.category_view, name="category"),
    path("bibliography", views.bibliography, name="bibliography"),
    path("abbreviations", views.abbreviations, name="abbreviations"),
    path("ages_at_death", views.ages_at_death, name="ages_at_death"),
    path("divine_sacred_beings", views.divine_sacred_beings, name="divine_sacred_beings"),
    path("emperors_imperial_family", views.emperors_imperial_family, name="emperors_imperial_family"),
    path("erasures", views.erasures, name="erasures"),
    path("findspots", views.findspots, name="findspots"),
    path("fragments", views.fragments, name="fragments"),
    path("organizations", views.organizations, name="organizations"),
    path("people", views.people, name="people"),
    path("personal_names", views.personal_names, name="personal_names"),
    path("place_names", views.place_names, name="place_names"),
    path("symbols", views.symbols, name="symbols"),
    path("words", views.words, name="words")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)