# Generated by Django 3.1.5 on 2021-01-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xwzx', '0004_auto_20210130_1203'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SYImg',
        ),
        migrations.AlterField(
            model_name='hynew',
            name='published_time',
            field=models.DateTimeField(verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='jtnew',
            name='published_time',
            field=models.DateTimeField(verbose_name='发布时间'),
        ),
    ]