# Generated by Django 4.1.3 on 2023-02-09 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dbs',
            old_name='emp_id',
            new_name='wid',
        ),
    ]
