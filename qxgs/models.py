from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import os, re
from django.conf import settings


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
# Create your models here.

class QXgs(models.Model):

    objects = ImgQuerySet.as_manager()
    qxgs_name = models.CharField('旗下公司名称', max_length=50, unique=True)
    simple_content = models.TextField('公司简介', max_length=1000)
    img = models.ImageField("封面", upload_to='cover_img/%Y%m%d')
    content = RichTextUploadingField("公司介绍")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        verbose_name = '旗下公司'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return self.qxgs_name

    def delete(self, *args, **kwargs):

        upload_list = re.findall(r'img.*?src="(.*?)"|video.*?src="(.*?)"', self.content)
        for uploads in upload_list:
            for upload in uploads:
                if(upload!=''):
                    os.remove(settings.UPLOAD_DIR+upload)

        self.img.delete()

        return super().delete(*args, **kwargs)


