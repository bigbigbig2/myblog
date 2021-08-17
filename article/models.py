#Model存取数据，View决定需要调取哪些数据，而Template则负责将调取出的数据以合理的方式展现出来。
from django.db import models
# timezone 用于处理时间相关事务。
from django.utils import timezone
# 导入内建的User模型
from django.contrib.auth.models import User
from markdown import Markdown


class Tag(models.Model):
    """文章标签"""
    #类似于MySQL中的varchar
    text = models.CharField(max_length=30)
    #定义其排序
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text


class Category(models.Model):
    """文章分类"""
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

#将标题图设为一个独立的模型
class Avatar(models.Model):
    #%Y%m%d是日期格式化的写法，会最终格式化为系统时间
    #ImageField字段不会存储图片本身，而仅仅保存图片的地址
    content = models.ImageField(upload_to='avatar/%Y%m%d')


class Article(models.Model):
    """博客文章 model"""
    #设置外键
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    # 分类
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )
    # 标签
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='articles'
    )
    # 标题图
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article'
    )
    # 标题
    title = models.CharField(max_length=100)
    # 正文
    body = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    # 新增方法，将 body 转换为带 html 标签的正文
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        #返回的是已渲染为 html 的正文和目录
        return md_body, md.toc
