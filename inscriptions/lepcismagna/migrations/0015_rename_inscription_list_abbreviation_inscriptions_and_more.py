# Generated by Django 5.0 on 2023-12-14 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lepcismagna', '0014_remove_abbreviation_inscriptions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abbreviation',
            old_name='inscription_list',
            new_name='inscriptions',
        ),
        migrations.RenameField(
            model_name='epigraphicreference',
            old_name='inscription_list',
            new_name='inscriptions',
        ),
    ]
