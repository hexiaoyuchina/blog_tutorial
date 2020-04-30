from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name='分类')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name
class Tag(models.Model):
    name=models.CharField(max_length=200,verbose_name='标签')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name
class post(models.Model):
    title=models.CharField(max_length=100,verbose_name='博客标题')
    body=models.TextField(verbose_name='博客正文')
    created_time=models.DateTimeFieldField(verbose_name='创建日期')
    modified_time=models.DateTimeField(verbose_name='修改日期')
    excerpt=models.CharField(max_length=200,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=
