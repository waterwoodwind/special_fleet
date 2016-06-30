#coding=utf-8
import os
import sys
sys.path.append("F:\\github\\special_fleet")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "special_fleet.settings")

import django
django.setup()
from car_record.models import *

def import_Human():
    f = open('Human.txt')
    txt = f.read().decode('GBK')
    objectList = []
    title = txt.split('\n')
    print title
    for item in title:
        department = Human(name=item)
        objectList.append(department)
    Human.objects.bulk_create(objectList)

if __name__ == "__main__":
    import_Human()
    print('Done!')