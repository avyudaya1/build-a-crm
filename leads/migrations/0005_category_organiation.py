# Generated by Django 3.1.4 on 2021-06-08 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20210608_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='organiation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]
