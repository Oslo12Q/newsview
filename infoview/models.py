# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NewsInfo(models.Model):
    LMLX_CHOICES = (
        (u'矿业动态', u'矿业动态'),
        (u'图片资讯', u'图片资讯'),
        (u'合作信息', u'合作信息'),
        (u'案例分析', u'案例分析'),
        (u'风土人情', u'风土人情'),
        (u'境外项目', u'境外项目'),
    )
    WZXX_BT = models.CharField(u"标题", max_length=255, default='')
    #WZXX_FBSJ = models.DateField(u"发布时间", default='')
    WZXX_FBSJ = models.CharField(u"发布时间", max_length=10, default='')
    WZXX_FBNER = models.TextField(u"正文", )
    WZXX_Lang = models.CharField(u"语种", max_length=20, default='')
    WZXX_LY = models.CharField(u"新闻来源", max_length=255, default='')
    WZXX_URL = models.URLField(u"来源网址", max_length=255, default='')
    # WZXX_URL = models.TextField(u"来源网址", )
    WZXX_BK = models.CharField(u"新闻版块", max_length=50, choices=LMLX_CHOICES, default=u'矿业动态')
    WZXX_CT = models.DateTimeField(u"爬取时间", auto_now_add=True, editable=False)
    WZXX_FBZT = models.BooleanField(u"发布状态", default=False)
    #WZXX_BY_ONE = models.ManyToManyField(KcCountry, verbose_name=u'新闻提及国家', blank=True)
