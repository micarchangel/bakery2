# Generated by Django 5.0.6 on 2024-06-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
