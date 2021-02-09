
import os, sys
import django
django.setup()
from  django.db import DatabaseError
from parser_site.parsing import *


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append((proj))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")


# catalog_onesie_bodysuit_skirt_sets('https://www.littleforbig.com/product-category/clothes/adult-onesie-bodysuits/onesie-bodysuit-skirt-sets/')


product_card_info('https://www.littleforbig.com/product/cosplay-magical-girls-pink-onesie-skirt-set/')
# site_joblab('https://joblab.ru/search.php?r=vac&srprofecy=%CF%F0%EE%E3%F0%E0%EC%EC%E8%F1%F2&kw_w2=1&srzpmin=&srregion=26&srcity=305&srcategory=&submit=1')
#