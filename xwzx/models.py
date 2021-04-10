from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import os, re
from django.conf import settings
from django.core.cache import cache


class TextQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        
        for img_QuerySet in self:

            upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', img_QuerySet.content)
            for uploads in upload_list:
                for upload in uploads:
                    if(upload!=''):
                        os.remove(settings.UPLOAD_DIR+upload)

            # img_QuerySet.img.delete()

        super().delete(*args, **kwargs)

        all_pager = JTNew.objects.all().count()
        cache.set("JTNew_count", all_pager, None)
# Create your models here.


class JTNew(models.Model):

    objects = TextQuerySet.as_manager()
    title = models.CharField("标题", max_length=50)
    author = models.CharField("作者", max_length=50)
    # img = models.ImageField("封面", upload_to='cover_img/%Y%m%d', blank=True)
    content = RichTextUploadingField("内容")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    published_time = models.DateTimeField("发布时间")

    class Meta:
        verbose_name = '集团新闻'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return self.title

    def delete(self, *args, **kwargs):

        upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', self.content)
        for uploads in upload_list:
            for upload in uploads:
                if(upload!=''):
                    os.remove(settings.UPLOAD_DIR+upload)

        super().delete(*args, **kwargs)

        all_pager = JTNew.objects.all().count()
        cache.set("JTNew_count", all_pager, None)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        all_pager = JTNew.objects.all().count()
        cache.set("JTNew_count", all_pager, None)



# class HYNew(models.Model):

#     objects = TextQuerySet.as_manager()
#     title = models.CharField("标题", max_length=50)
#     author = models.CharField("作者", max_length=50)
#     # img = models.ImageField("封面", upload_to='cover_img/%Y%m%d', blank=True)
#     content = RichTextUploadingField("内容")
#     created_time = models.DateTimeField("创建时间", auto_now_add=True)
#     published_time = models.DateTimeField("发布时间")

#     class Meta:
#         verbose_name = '行业新闻'
#         verbose_name_plural = verbose_name

#     def delete(self, *args, **kwargs):

#         upload_list = re.findall(r'img alt="" src="(.*?)"', self.content)
#         for upload in upload_list:
#             os.remove(settings.UPLOAD_DIR+upload)

#         return super().delete(*args, **kwargs)


class ImgQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        
        for img_QuerySet in self:

            upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', img_QuerySet.content)
            for uploads in upload_list:
                for upload in uploads:
                    if(upload!=''):
                        os.remove(settings.UPLOAD_DIR+upload)

            img_QuerySet.img.delete()

        super().delete(*args, **kwargs)

        all_pager = IMGNew.objects.all().count()
        cache.set("IMGNew_count", all_pager, None)


class IMGNew(models.Model):

    objects = ImgQuerySet.as_manager()
    title = models.CharField("标题", max_length=50)
    author = models.CharField("作者", max_length=50)
    img = models.ImageField("封面", upload_to='cover_img/%Y%m%d')
    content = RichTextUploadingField("内容")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    published_time = models.DateTimeField("发布时间")

    class Meta:
        verbose_name = '图片新闻'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return self.title
        
    def delete(self, *args, **kwargs):

        upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', self.content)
        for uploads in upload_list:
            for upload in uploads:
                if(upload!=''):
                    os.remove(settings.UPLOAD_DIR+upload)

        self.img.delete()

        super().delete(*args, **kwargs)

        all_pager = IMGNew.objects.all().count()
        cache.set("IMGNew_count", all_pager, None)
    
    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        all_pager = IMGNew.objects.all().count()
        cache.set("IMGNew_count", all_pager, None)
# class LDNew(models.Model):

#     objects = ImgQuerySet.as_manager()
#     title = models.CharField("标题", max_length=50)
#     author = models.CharField("作者", max_length=50)
#     img = models.ImageField("封面", upload_to='cover_img/%Y%m%d', blank=True)
#     content = RichTextUploadingField("内容")
#     created_time = models.DateTimeField("创建时间", auto_now_add=True)
#     published_time = models.DateField("发布时间")

#     class Meta:
#         verbose_name = '公司领导动态'
#         verbose_name_plural = verbose_name

#     def delete(self, *args, **kwargs):

#         upload_list = re.findall(r'img alt="" src="(.*?)"', self.content)
#         for upload in upload_list:
#             os.remove(upload_dir+upload)

#         self.img.delete()

#         return super().delete(*args, **kwargs)


# class SYNew(models.Model):

#     objects = ImgQuerySet.as_manager()
#     title = models.CharField("标题", max_length=50)
#     author = models.CharField("作者", max_length=50)
#     img = models.ImageField("封面", upload_to='cover_img/%Y%m%d', blank=True)
#     content = RichTextUploadingField("内容")
#     created_time = models.DateTimeField("创建时间", auto_now_add=True)
#     published_time = models.DateField("发布时间")

#     class Meta:
#         verbose_name = '首页新闻'
#         verbose_name_plural = verbose_name

#     def delete(self, *args, **kwargs):

#         upload_list = re.findall(r'img alt="" src="(.*?)"', self.content)
#         for upload in upload_list:
#             os.remove(settings.UPLOAD_DIR+upload)

#         self.img.delete()

#         return super().delete(*args, **kwargs)

