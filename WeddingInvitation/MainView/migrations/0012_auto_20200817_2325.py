# Generated by Django 3.0.8 on 2020-08-17 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainView', '0011_auto_20200817_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmanswer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
