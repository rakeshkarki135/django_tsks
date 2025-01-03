# Generated by Django 5.1.4 on 2024-12-30 05:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Superuser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'superuser',
                'verbose_name_plural': 'superusers',
            },
            bases=('nerd.customuser',),
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
    ]