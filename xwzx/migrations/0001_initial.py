# Generated by Django 3.1.2 on 2021-01-26 03:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HYNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('img', models.ImageField(blank=True, upload_to='cover_img/%Y%m%d', verbose_name='封面')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('published_time', models.DateField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '行业新闻',
                'verbose_name_plural': '行业新闻',
            },
        ),
        migrations.CreateModel(
            name='JTNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('img', models.ImageField(blank=True, upload_to='cover_img/%Y%m%d', verbose_name='封面')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('published_time', models.DateField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '集团新闻',
                'verbose_name_plural': '集团新闻',
            },
        ),
        migrations.CreateModel(
            name='LDNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('img', models.ImageField(blank=True, upload_to='cover_img/%Y%m%d', verbose_name='封面')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('published_time', models.DateField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '公司领导动态',
                'verbose_name_plural': '公司领导动态',
            },
        ),
        migrations.CreateModel(
            name='SYNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('img', models.ImageField(blank=True, upload_to='cover_img/%Y%m%d', verbose_name='封面')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('published_time', models.DateField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '首页新闻',
                'verbose_name_plural': '首页新闻',
            },
        ),
    ]