# Generated by Django 3.0.3 on 2020-02-20 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200220_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='modified_by',
        ),
    ]
