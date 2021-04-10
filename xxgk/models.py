from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import os, re
from django.conf import settings
from django.core.cache import cache

class ImgQuerySet(models.QuerySet):

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

class XXgk_RC(models.Model):

    objects = ImgQuerySet.as_manager()
    # xxgk_type = models.CharField("类型", choices=choice_list, max_length=50)
    content = RichTextUploadingField("内容")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    published_time = models.DateTimeField("发布时间")

    class Meta:
        verbose_name = '人才招聘'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return '人才招聘'

    def delete(self, *args, **kwargs):

        upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', self.content)
        for uploads in upload_list:
            for upload in uploads:
                if(upload!=''):
                    os.remove(settings.UPLOAD_DIR+upload)

        # self.img.delete()

        return super().delete(*args, **kwargs)


class Img_GGQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        
        for img_QuerySet in self:
            upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', img_QuerySet.content)
            for uploads in upload_list:
                for upload in uploads:
                    if(upload!=''):
                        os.remove(settings.UPLOAD_DIR+upload)
            # img_QuerySet.img.delete()
        super().delete(*args, **kwargs)

        all_pager = XXgk_GG.objects.all().count()
        cache.set("XXgk_GG_count", all_pager, None)


class XXgk_GG(models.Model):

    objects = Img_GGQuerySet.as_manager()
    title = models.CharField("公告标题", max_length=50)
    content = RichTextUploadingField("内容")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    published_time = models.DateTimeField("发布时间")

    class Meta:
        verbose_name = '集团公告'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return self.title

    def delete(self, *args, **kwargs):

        upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', self.content)
        for uploads in upload_list:
            for upload in uploads:
                if(upload!=''):
                    os.remove(settings.UPLOAD_DIR+upload)

        # self.img.delete()

        super().delete(*args, **kwargs)

        all_pager = XXgk_GG.objects.all().count()
        cache.set("XXgk_GG_count", all_pager, None)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        all_pager = XXgk_GG.objects.all().count()
        cache.set("XXgk_GG_count", all_pager, None)



