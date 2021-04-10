# Generated by Django 3.1.5 on 2021-01-30 15:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xwzx', '0005_auto_20210130_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMGNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('img', models.ImageField(upload_to='cover_img/%Y%m%d', verbose_name='封面')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('published_time', models.DateTimeField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '封面新闻',
                'verbose_name_plural': '封面新闻',
            },
        ),
    ]