from django.shortcuts import render
from car_record.models import car_record
from django.core import serializers
from django.http import HttpResponse
import json
# Create your views here.
def home(request):
    query_data = car_record.objects.all().order_by('-start_datetime')
    json_data = serializers.serialize("json", query_data, use_natural_foreign_keys=True)
    list_data = json.loads(json_data)
    return HttpResponse(json_data)
