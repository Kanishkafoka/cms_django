# Generated by Django 5.0.1 on 2024-02-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0008_alter_author_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_type',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
