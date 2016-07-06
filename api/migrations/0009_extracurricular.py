# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 12:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_achievement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_e', models.TextField(blank=True, null=True)),
                ('org_e', models.TextField(blank=True, null=True)),
                ('details_e', models.TextField(blank=True, null=True)),
                ('year_v', models.TextField(blank=True, null=True)),
                ('org_v', models.TextField(blank=True, null=True)),
                ('details_v', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
