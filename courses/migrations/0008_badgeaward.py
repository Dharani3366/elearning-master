# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-21 15:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0007_auto_20200719_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awarded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='badges_earned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
