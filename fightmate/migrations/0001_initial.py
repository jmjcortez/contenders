# Generated by Django 2.1.7 on 2019-10-16 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('gender', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_state', models.DateTimeField()),
                ('text', models.TextField(blank=True)),
                ('is_last', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bio',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'discipline',
            },
        ),
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fight_time', models.DateTimeField()),
                ('result_fighter_1', models.CharField(blank=True, max_length=100, null=True)),
                ('result_fighter_2', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fightmate.Discipline')),
                ('fighter_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='first_fighters', to=settings.AUTH_USER_MODEL)),
                ('fighter_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='second_fighters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fight',
            },
        ),
        migrations.CreateModel(
            name='UserDiscipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_of_experience', models.IntegerField()),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fightmate.Discipline')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_discipline',
            },
        ),
    ]
