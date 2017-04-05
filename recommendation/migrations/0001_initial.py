# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('keyword_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('imdb_id', models.CharField(blank=True, max_length=9, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=32, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('vote_average', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('popularity', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('vote_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MovieCast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_character', models.CharField(blank=True, max_length=300, null=True)),
                ('cast_order', models.IntegerField(blank=True, null=True)),
                ('cast_id', models.IntegerField(blank=True, null=True)),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Movie')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MovieCrew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=25, null=True)),
                ('job', models.CharField(blank=True, max_length=70, null=True)),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Movie')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Genre')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Movie')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MovieKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Keyword')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Movie')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.IntegerField(primary_key=True, serialize=False)),
                ('imdb_id', models.CharField(blank=True, max_length=11, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('deathday', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('place_of_birth', models.CharField(blank=True, max_length=150, null=True)),
                ('popularity', models.DecimalField(blank=True, decimal_places=6, max_digits=11, null=True)),
                ('profile_path', models.CharField(blank=True, max_length=34, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='moviecrew',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Person'),
        ),
        migrations.AddField(
            model_name='moviecast',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Person'),
        ),
    ]
