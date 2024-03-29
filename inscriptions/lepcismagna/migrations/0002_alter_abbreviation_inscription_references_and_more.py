# Generated by Django 5.0 on 2023-12-06 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('lepcismagna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abbreviation',
            name='inscription_references',
            field=models.ManyToManyField(blank=True, null=True, through='lepcismagna.InscriptionAbbreviation', to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='ageatdeath',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='bibliography',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='category',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='divinesacredbeing',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='emperorimperialfamily',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='epigraphicreference',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, through='lepcismagna.InscriptionReference', to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='erasure',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='findspot',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='fragment',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='abbreviations',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.abbreviation'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='age_at_death',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.ageatdeath'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='associated_inscr',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='bibliography_entries',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.bibliography'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.category'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='divine_sacred_beings',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.divinesacredbeing'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='emperors_imperial_family',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.emperorimperialfamily'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='erasures',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.erasure'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='findspots',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.findspot'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='fragments',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.fragment'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.image'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='organizations',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.organization'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='people',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.person'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='personal_names',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.personalname'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='place_names',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.placename'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='symbols',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.symbol'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='words',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.word'),
        ),
        migrations.AlterField(
            model_name='inscriptionabbreviation',
            name='abbreviation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.abbreviation'),
        ),
        migrations.AlterField(
            model_name='inscriptionabbreviation',
            name='inscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='inscriptionbibliography',
            name='bibliography',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.bibliography'),
        ),
        migrations.AlterField(
            model_name='inscriptionbibliography',
            name='inscriptions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='inscriptionreference',
            name='inscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='inscriptionreference',
            name='reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.epigraphicreference'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='person',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='personalname',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='placename',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dossier',
            field=models.ManyToManyField(blank=True, null=True, related_name='dossiers', to='lepcismagna.inscription'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_groups', related_query_name='user_group', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_permissions', related_query_name='user_permission', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='word',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, null=True, to='lepcismagna.inscription'),
        ),
    ]
