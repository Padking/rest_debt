# Generated by Django 3.0.4 on 2020-03-29 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debt_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debtor',
            old_name='name',
            new_name='debtor_name',
        ),
    ]