# Generated by Django 5.0.6 on 2024-06-16 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('tel', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
