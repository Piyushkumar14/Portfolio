# Generated by Django 5.1.4 on 2025-01-08 12:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
