# Generated by Django 5.2 on 2025-05-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_workout_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
