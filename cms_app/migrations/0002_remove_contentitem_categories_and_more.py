# Generated by Django 5.0.1 on 2024-02-16 05:26

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentitem',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='contentitem',
            name='summary',
        ),
        migrations.AddField(
            model_name='contentitem',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contentitem',
            name='body',
            field=models.TextField(max_length=300, validators=[django.core.validators.MaxLengthValidator(300)]),
        ),
        migrations.AlterField(
            model_name='contentitem',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(30)]),
        ),
    ]