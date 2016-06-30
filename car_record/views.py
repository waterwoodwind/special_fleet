#coding=utf-8
from django.shortcuts import render
from car_record.models import car_record
from django.core import serializers
from django.http import HttpResponse
import json
import datetime
# Create your views here.
def home(request):
    query_data = car_record.objects.all().order_by('-start_datetime')
    json_data = serializers.serialize("json", query_data, use_natural_foreign_keys=True)
    list_data = json.loads(json_data)

    dict_name_verbose_name = {}
    for field in car_record._meta.fields:
        dict_name_verbose_name[field.name] = field.verbose_name

    upload_data = []
    for item in list_data:
        single_data = item['fields']
        single_data[u'id'] = item['pk']
        upload_data.append(single_data)

    chinese_updata = []
    for item in upload_data:
        dict_updata = {}
        for key, value in item.items():
            dict_updata[dict_name_verbose_name[key]] = value

            # print chinese_updata
        dict_updata[u"出发日期"] = dict_updata[u"开始时间"][0:10]
        dict_updata[u"出发时间"] = dict_updata[u"开始时间"][11:19]
        dict_updata[u"收车日期"] = dict_updata[u"结束时间"][0:10]
        dict_updata[u"收车时间"] = dict_updata[u"结束时间"][11:19]
        chinese_updata.append(dict_updata)


    upload_data = json.dumps(chinese_updata)
    # 统计今日的每人工时数
    today = datetime.date.today()
    delta = datetime.timedelta(days=1)
    tomorrow = today + delta
    count_obj = car_record.objects.filter(start_datetime__range =(datetime.date.today(), tomorrow))
    count_data = serializers.serialize("json", count_obj, use_natural_foreign_keys=True)
    count_data = json.loads(count_data)
    print count_data
    count_sum = {}
    for single_data in count_data:
        item = single_data[u"fields"]
        if item["worker"] not in count_sum:
            count_sum[item["worker"]] = item["task_time"]
        else:
            count_sum[item["worker"]] = count_sum[item["worker"]] + item["task_time"]

    print count_sum
    upload_dict = {}
    upload_list = []
    for key,value in count_sum.items():
        upload_dict = {}
        upload_dict["worker"] = key
        upload_dict["sum"] = value
        upload_list.append(upload_dict)
    json_sum = json.dumps(upload_list)

    return render(request, 'home.html', {'json_data': upload_data, 'json_sum': json_sum})
