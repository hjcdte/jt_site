from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import os, re
from django.conf import settings


class CharQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        
        for img_QuerySet in self:

            upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', img_QuerySet.content)
            for uploads in upload_list:
                for upload in uploads:
                    if(upload!=''):
                        os.remove(settings.UPLOAD_DIR+upload)

            # img_QuerySet.img.delete()

        return super().delete(*args, **kwargs)
# Create your models here.

choice_list = [('jtjj','集团简介'),
            ('zzjg','组织机构'),('zyyw','主营业务'),
            # ('ppxx','品牌形象'),('jtgc','集团高层'),
]

class GYwm(models.Model):

    objects = CharQuerySet.as_manager()
    gywm_type = models.CharField("类型", choices=choice_list, max_length=50)
    # img = models.ImageField("照片(用于品牌形象和集团高层)", upload_to='cover_img/%Y%m%d',blank=True)
    content = RichTextUploadingField("内容")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        verbose_name = '关于我们'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return self.gywm_type

    def delete(self, *args, **kwargs):

        upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', self.content)
        for uploads in upload_list:
            for upload in uploads:
                if(upload!=''):
                    os.remove(settings.UPLOAD_DIR+upload)
        # self.img.delete()

        return super().delete(*args, **kwargs)


class ImgQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        
        for img_QuerySet in self:

            upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', img_QuerySet.content)
            for uploads in upload_list:
                for upload in uploads:
                    if(upload!=''):
                        os.remove(settings.UPLOAD_DIR+upload)

            img_QuerySet.img.delete()

        return super().delete(*args, **kwargs)


class GYwm_XX(models.Model):

    objects = ImgQuerySet.as_manager()
    name = models.CharField('品牌名称(用于后台辨认)', max_length=50, unique=True)
    # gywm_type = models.CharField("类型", choices=choice_list, max_length=50)
    img = models.ImageField("品牌照片", upload_to='cover_img/%Y%m%d')
    content = RichTextUploadingField("品牌介绍")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        verbose_name = '品牌介绍'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return self.name

    def delete(self, *args, **kwargs):

        upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', self.content)
        for uploads in upload_list:
            for upload in uploads:
                if(upload!=''):
                    os.remove(settings.UPLOAD_DIR+upload)
        
        self.img.delete()

        return super().delete(*args, **kwargs)


class GYwm_GC(models.Model):

    objects = ImgQuerySet.as_manager()
    name = models.CharField('领导姓名(用于后台辨认)', max_length=50, unique=True)
    # gywm_type = models.CharField("类型", choices=choice_list, max_length=50)
    img = models.ImageField("领导照片", upload_to='cover_img/%Y%m%d')
    content = RichTextUploadingField("领导介绍")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        verbose_name = '集团高层'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return self.name
        
    def delete(self, *args, **kwargs):

        upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', self.content)
        for uploads in upload_list:
            for upload in uploads:
                if(upload!=''):
                    os.remove(settings.UPLOAD_DIR+upload)

        self.img.delete()

        return super().delete(*args, **kwargs)
