from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import os, re
from django.conf import settings


class ImgSet(models.QuerySet):

    def delete(self, *args, **kwargs):
        
        for img_QuerySet in self:

            # upload_list = re.findall(r'img alt="" src="(.*?)"', img_QuerySet.content)
            # for upload in upload_list:
            #     os.remove(settings.UPLOAD_DIR+upload)

            img_QuerySet.img.delete()

        return super().delete(*args, **kwargs)
# Create your models here.

class Cp_Type(models.Model):

    objects = ImgSet.as_manager()
    cp_type = models.CharField("产品类型", max_length=50, unique=True)
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    img = models.ImageField("封面", upload_to='cover_img/%Y%m%d')
    # content = RichTextUploadingField("内容")
    content = models.TextField('内容', max_length=1000)

    class Meta:
        verbose_name = '产品类型'
        verbose_name_plural = verbose_name
    
    def  __str__(self):
        return self.cp_type
    
    def delete(self, *args, **kwargs):

        # upload_list = re.findall(r'img alt="" src="(.*?)"', self.content)
        # for upload in upload_list:
        #     os.remove(settings.UPLOAD_DIR+upload)

        self.img.delete()

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


class Cp(models.Model):

    objects = ImgQuerySet.as_manager()
    cp_name = models.CharField("产品名称", max_length=50,unique=True)
    cp_type = models.ForeignKey(Cp_Type, on_delete=models.CASCADE,verbose_name='产品类型')
    img = models.ImageField("封面", upload_to='cover_img/%Y%m%d')
    option = models.BooleanField("是否上首页(六个)")
    content = RichTextUploadingField("内容")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return self.cp_name

    def delete(self, *args, **kwargs):

        upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', self.content)
        for uploads in upload_list:
            for upload in uploads:
                if(upload!=''):
                    os.remove(settings.UPLOAD_DIR+upload)

        self.img.delete()

        return super().delete(*args, **kwargs)

