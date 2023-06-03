# Generated by Django 4.2.1 on 2023-06-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0008_alter_donerrequest_stutas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donerrequest',
            name='stutas',
            field=models.CharField(blank=True, choices=[(None, 'Select'), ('ACCEPT', 'ACCEPT'), ('REJECT', 'REJECT')], max_length=10, null=True),
        ),
    ]
