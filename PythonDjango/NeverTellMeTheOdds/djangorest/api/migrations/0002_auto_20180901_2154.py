# Generated by Django 2.1 on 2018-09-01 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singlebet',
            old_name='gambler',
            new_name='name',
        ),
    ]