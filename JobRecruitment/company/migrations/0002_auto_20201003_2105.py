# Generated by Django 3.1.2 on 2020-10-03 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='skill1',
            new_name='skillsReqd',
        ),
        migrations.RemoveField(
            model_name='job',
            name='skill2',
        ),
        migrations.RemoveField(
            model_name='job',
            name='skill3',
        ),
    ]
