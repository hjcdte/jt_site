# Generated by Django 3.1.5 on 2021-02-05 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xxgk', '0003_auto_20210203_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xxgk_gg',
            old_name='name',
            new_name='title',
        ),
    ]
