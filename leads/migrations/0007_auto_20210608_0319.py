# Generated by Django 3.1.4 on 2021-06-08 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_auto_20210608_0253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='organiation',
            new_name='organisation',
        ),
    ]
