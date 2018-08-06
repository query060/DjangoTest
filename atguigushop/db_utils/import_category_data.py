import os
import sys


#独立使用models
filename_path=os.path.realpath(__file__)
print('filename_path==',filename_path)
dirname=os.path.dirname(filename_path)
sys.path.insert(0,dirname)
print(sys.path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atguigushop.settings")

import django

django.setup()

from goods.models import GoodsCategory
from db_utils.data.category_data import row_data

# all_GoodsCategory=GoodsCategory.objects.all()
# print(all_GoodsCategory)
for item in row_data:
    instance1=GoodsCategory()
    instance1.name=item['name']
    instance1.code=item['code']
    instance1.category_type=1
    instance1.save()

    for item2 in item["sub_categorys"]:
        instance2=GoodsCategory()
        instance2.name=item2["name"]
        instance2.code=item2["code"]
        instance2.category_type = 2
        instance2.parent_category=instance1

        instance2.save()

        for item3 in item2["sub_categorys"]:
            instance3 = GoodsCategory()
            instance3.name = item3["name"]
            instance3.code = item3["code"]
            instance3.category_type = 3
            instance3.parent_category = instance2

            instance3.save()



