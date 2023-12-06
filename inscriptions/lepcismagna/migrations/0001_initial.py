# Generated by Django 5.0 on 2023-12-06 16:01

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abbreviation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(blank=True, max_length=20)),
                ('expansion', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AgeAtDeath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'ages at death',
            },
        ),
        migrations.CreateModel(
            name='Bibliography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(blank=True, max_length=50)),
                ('entry', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'bibliographies',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='DivineSacredBeing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divine_being', models.CharField(blank=True, max_length=50)),
                ('epithet', models.CharField(blank=True, max_length=50)),
                ('external_resource', models.URLField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'divine and sacred beings',
            },
        ),
        migrations.CreateModel(
            name='EmperorImperialFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(blank=True, max_length=50)),
                ('epithet', models.CharField(blank=True, max_length=50)),
                ('external_resource', models.URLField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'emperors and imperial families',
            },
        ),
        migrations.CreateModel(
            name='EpigraphicReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(blank=True, max_length=50)),
                ('entry', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Erasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erased_text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Findspot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('findspots_upper', models.CharField(blank=True, max_length=255)),
                ('findspots_intermediate', models.CharField(blank=True, max_length=255)),
                ('findspots_lower', models.CharField(blank=True, max_length=255)),
                ('gazetteer', models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fragment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fragment', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_url', models.URLField(blank=True, max_length=255)),
                ('caption', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_creation_time', models.DateTimeField(auto_now_add=True)),
                ('is_validated', models.BooleanField(default=False)),
                ('inscription_id', models.CharField(blank=True, max_length=20)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('text', models.TextField(blank=True)),
                ('letters', models.TextField(blank=True)),
                ('date', models.CharField(max_length=50)),
                ('findspot_desc', models.TextField(blank=True)),
                ('original_location', models.CharField(max_length=255)),
                ('last_recorded_location', models.CharField(max_length=255)),
                ('transcription_interpretive', models.TextField(blank=True)),
                ('transcription_diplomatic', models.TextField(blank=True)),
                ('transcription_appcrit', models.TextField(blank=True)),
                ('translation_english', models.TextField(blank=True)),
                ('commentary', models.TextField(blank=True)),
                ('bibliography_text', models.TextField(blank=True)),
                ('abbreviations', models.ManyToManyField(blank=True, to='lepcismagna.abbreviation')),
                ('age_at_death', models.ManyToManyField(blank=True, to='lepcismagna.ageatdeath')),
                ('associated_inscr', models.ManyToManyField(blank=True, to='lepcismagna.inscription')),
                ('bibliography_entries', models.ManyToManyField(blank=True, to='lepcismagna.bibliography')),
                ('categories', models.ManyToManyField(blank=True, to='lepcismagna.category')),
                ('divine_sacred_beings', models.ManyToManyField(blank=True, to='lepcismagna.divinesacredbeing')),
                ('emperors_imperial_family', models.ManyToManyField(blank=True, to='lepcismagna.emperorimperialfamily')),
                ('erasures', models.ManyToManyField(blank=True, to='lepcismagna.erasure')),
                ('findspots', models.ManyToManyField(blank=True, to='lepcismagna.findspot')),
                ('fragments', models.ManyToManyField(blank=True, to='lepcismagna.fragment')),
                ('images', models.ManyToManyField(blank=True, to='lepcismagna.image')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='inscription_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription'),
        ),
        migrations.AddField(
            model_name='fragment',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, to='lepcismagna.inscription'),
        ),
        migrations.AddField(
            model_name='findspot',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, to='lepcismagna.inscription'),
        ),
        migrations.AddField(
            model_name='erasure',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, to='lepcismagna.inscription'),
        ),
        migrations.AddField(
            model_name='emperorimperialfamily',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, to='lepcismagna.inscription'),
        ),
        migrations.AddField(
            model_name='divinesacredbeing',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, to='lepcismagna.inscription'),
        ),
        migrations.AddField(
            model_name='category',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, to='lepcismagna.inscription'),
        ),
        migrations.AddField(
            model_name='bibliography',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, to='lepcismagna.inscription'),
        ),
        migrations.AddField(
            model_name='ageatdeath',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, to='lepcismagna.inscription'),
        ),
        migrations.CreateModel(
            name='InscriptionAbbreviation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number_reference', models.CharField(blank=True, max_length=50)),
                ('abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.abbreviation')),
                ('inscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription')),
            ],
        ),
        migrations.AddField(
            model_name='abbreviation',
            name='inscription_references',
            field=models.ManyToManyField(blank=True, through='lepcismagna.InscriptionAbbreviation', to='lepcismagna.inscription'),
        ),
        migrations.CreateModel(
            name='InscriptionBibliography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number_references', models.CharField(max_length=50)),
                ('bibliography', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.bibliography')),
                ('inscriptions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription')),
            ],
            options={
                'verbose_name_plural': 'inscription bibliographies',
            },
        ),
        migrations.CreateModel(
            name='InscriptionReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(blank=True, max_length=20)),
                ('inscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.inscription')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.epigraphicreference')),
            ],
        ),
        migrations.AddField(
            model_name='epigraphicreference',
            name='inscriptions',
            field=models.ManyToManyField(blank=True, through='lepcismagna.InscriptionReference', to='lepcismagna.inscription'),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('epithets', models.CharField(blank=True, max_length=50)),
                ('external_resource', models.URLField(blank=True, max_length=255)),
                ('inscriptions', models.ManyToManyField(blank=True, to='lepcismagna.inscription')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='organizations',
            field=models.ManyToManyField(blank=True, to='lepcismagna.organization'),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(blank=True, max_length=100)),
                ('external_resource', models.CharField(blank=True, max_length=255)),
                ('inscriptions', models.ManyToManyField(blank=True, to='lepcismagna.inscription')),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.AddField(
            model_name='inscription',
            name='people',
            field=models.ManyToManyField(blank=True, to='lepcismagna.person'),
        ),
        migrations.CreateModel(
            name='PersonalName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('inscriptions', models.ManyToManyField(blank=True, to='lepcismagna.inscription')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='personal_names',
            field=models.ManyToManyField(blank=True, to='lepcismagna.personalname'),
        ),
        migrations.CreateModel(
            name='PlaceName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(blank=True, max_length=100)),
                ('attested_form', models.CharField(blank=True, max_length=100)),
                ('toponym_ethnic', models.CharField(blank=True, max_length=10)),
                ('external_resource', models.URLField(blank=True, max_length=255)),
                ('inscriptions', models.ManyToManyField(blank=True, to='lepcismagna.inscription')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='place_names',
            field=models.ManyToManyField(blank=True, to='lepcismagna.placename'),
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(blank=True, max_length=20)),
                ('inscriptions', models.ManyToManyField(blank=True, to='lepcismagna.inscription')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='symbols',
            field=models.ManyToManyField(blank=True, to='lepcismagna.symbol'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dossier', models.ManyToManyField(blank=True, related_name='dossiers', to='lepcismagna.inscription')),
                ('groups', models.ManyToManyField(blank=True, related_name='user_groups', related_query_name='user_group', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_permissions', related_query_name='user_permission', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='entry_creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lepcismagna.user'),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lemma', models.CharField(blank=True, max_length=20)),
                ('language_code', models.CharField(blank=True, max_length=2)),
                ('inscriptions', models.ManyToManyField(blank=True, to='lepcismagna.inscription')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='words',
            field=models.ManyToManyField(blank=True, to='lepcismagna.word'),
        ),
    ]
