from django.db import models

# Create your models here.
class SYImgQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        
        for img_QuerySet in self:
            img_QuerySet.img.delete()

        return super().delete(*args, **kwargs)


class SYImg(models.Model):

    objects = SYImgQuerySet.as_manager()
    img = models.ImageField("首页图片", upload_to='cover_img/%Y%m%d')
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    published_time = models.DateTimeField("发布时间")

    class Meta:
        verbose_name = '首页图片'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return "首页图片"

    def delete(self, *args, **kwargs):

        self.img.delete()

        return super().delete(*args, **kwargs)