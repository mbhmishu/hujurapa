# Generated by Django 4.2.1 on 2023-06-02 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0006_donerrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donerrequest',
            old_name='Recipient',
            new_name='recipient',
        ),
        migrations.AlterField(
            model_name='donerrequest',
            name='donor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donor', to=settings.AUTH_USER_MODEL),
        ),
    ]