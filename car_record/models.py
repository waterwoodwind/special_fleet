#coding=utf-8

from django.db import models

# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)

    def __unicode__(self):
        return self.name

class JobType(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)

    def __unicode__(self):
        return self.name

class car_record(models.Model):
    start_datetime = models.DateTimeField(verbose_name=u'开始时间')
    end_datetime = models.DateTimeField(verbose_name=u'结束时间')
    worker = models.ForeignKey(Human, verbose_name=u'工作者')
    job_type = models.ForeignKey(JobType, verbose_name =u'工作类型')
    job_content = models.CharField(max_length = 100, verbose_name=u'工作内容')
    car_id = models.CharField(max_length= 20, verbose_name=u'车牌号')
    task_time = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u'此次工时')

    def __unicode__(self):
        return self.job_content


