import requests
import codecs
from bs4 import BeautifulSoup as BS
import csv
from parser_site.models import *
import parser_site.user_agent_list as ua
from google_trans_new import google_translator
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'shop.settings'
site = 'https://www.littleforbig.com/product-category/clothes/'



#
# def pagination(url):
#     resp = requests.get(url, ua.rand_user_agent())
#     soup = BS(resp.content, 'html.parser')
#     i = 1
#     path_page = 'page/'
#     count_next_page = soup.find('ul', class_='page-numbers')
#     if count_next_page == None:
#         print(url + path_page + str(i) + '/')
#         catalog_onesie_bodysuit_skirt_sets(url + path_page + str(i) + '/')
#     else:
#         next = count_next_page.find('a', class_='next')
#         while i <= len(count_next_page)-1:
#             print(url + path_page + str(i) + '/')
#             catalog_onesie_bodysuit_skirt_sets(url + path_page + str(i) + '/')
#             i += 1
#
#
# def catalog_onesie_bodysuit_skirt_sets(url):
#     data, errors = [], []
#     resp = requests.get(url, ua.rand_user_agent())
#
#     if resp.status_code == 200:
#         soup = BS(resp.content, 'html.parser')
#         card_vac = soup.find_all('a', class_='woocommerce-LoopProduct-link')
#
#         for div in card_vac:
#             href = div['href']
#             print(href)
#             try:
#                 product_card_info(href)
#             except ValueError:
#                 print('Error')
#     else:
#         errors.append({'url': url, 'text': resp.text})
#
#
#     with open ('../littleforbig.csv', 'w', newline ='') as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerow(data)
#
#     h = codecs.open('../error_littleforbig.txt', 'w', 'utf-8')
#     h.write(str(errors))
#     h.close()
#
# def product_card_foto(url):
#     path = 'media/images/images-card/'
#     data = []
#     errors = []
#
#     resp = requests.get(url, ua.rand_user_agent())
#     print(resp.status_code)
#     if resp.status_code == 200:
#         soup = BS(resp.content, 'html.parser')
#         card_img = soup.find('div', class_='product-thumbnails')
#         card_vac = card_img.find_all('div', class_='col')
#
#         for div in card_vac:
#             image_thumb = div.find('img', class_='attachment-woocommerce_thumbnail')
#
#             if None in image_thumb.get_attribute_list('data-src'):
#                 photo_url = image_thumb.get_attribute_list('src')[0]
#             else:
#                 photo_url = image_thumb.get_attribute_list('data-src')[0]
#
#
#             save_data(path, get_name(photo_url), get_file(photo_url))
#
#             data.append(path + get_name(photo_url))
#
#         return data
#
#
#     else:
#         errors.append({'url': url, 'text': resp.text})
#     h = codecs.open('../error_littleforbig.txt', 'w', 'utf-8')
#     h.write(str(errors))
#     h.close()
#
#
# def product_card_info(url):
#     dollar = 100
#     path = 'media/images/images-card/'
#     data, errors = [], []
#     resp = requests.get(url, ua.rand_user_agent())
#     print(resp.status_code)
#     if resp.status_code == 200:
#         soup = BS(resp.content, 'html.parser')
#         translator = google_translator()
#         breadcump_cat = translator.translate(((soup.find('nav', class_='woocommerce-breadcrumb').find_all('a')[1].get_text()).title()), lang_tgt='ru')
#         breadcump_subcat = translator.translate(((soup.find('nav', class_='woocommerce-breadcrumb').find_all('a')[-1].get_text()).title()), lang_tgt='ru')
#
#         card_vac = soup.find('div', class_='product-info')
#         # title = translator.translate((card_vac.find('h1', class_='product-title').text).title().strip(), lang_tgt='ru')
#         title1 = card_vac.find('h1', class_='product-title').text.lower()
#         title = translator.translate(title1, lang_tgt='ru')
#
#
#         price = round(float(card_vac.find('bdi').text[1:])) * dollar
#
#
#
#         if CardProduct.objects.filter(url=url):
#             s = CardProduct.objects.get(url=url)
#             CardProduct.objects.filter(id=s.id).update(title=title, price=price)
#         else:
#             print('Товара не существует ' + url)
#
#
#         # Качаем фотки
#         # img_name = product_card_foto(url)
#
#
#         data.append({'title': title,
#                      'url': url,
#                      'price': price,
#                       })
#
#
#
#         try:
#             pass
#
#
#             # for i in img_name:
#             #     pic = CardFoto()
#             #     pic.product = s
#             #     pic.image = i
#             #     pic.save()
#         except ValueError:
#             print('Error save')
#
#     else:
#         errors.append({'url': url, 'text': resp.text})
#
#
#
#     return data, errors
#
#
#
#
#
# def parse_instagramm(url):
#     resp = requests.get(url, ua.rand_user_agent())
#     print(resp.status_code)
#     if resp.status_code == 200:
#         soup = BS(resp.content, 'html.parser')
#         card_vac = soup.find('img', class_='FFVAD')
#         return card_vac['src']
#
#
# def get_file(url):
#     response = requests.get(url, stream=True)
#     return response
#
#
# def save_data(path, name, file_data):
#     file = open(path + name, 'bw') #Бинарный режим, изображение передається байтами
#     for chunk in file_data.iter_content(4096): # Записываем в файл по блочно данные
#         file.write(chunk)
#
#
# def get_name(url):
#     name = url.split('/')[-1]
#     return name
#
# def get_name_category(url):
#     name = url.split('/')[-2]
#     return name
#
#
#
# def find_category(url):
#     resp = requests.get(url, ua.rand_user_agent())
#     soup = BS(resp.content, 'html.parser')
#     i = 1
#     menu = soup.find('ul', class_='product-categories')
#     category = menu.find_all('a')
#     for item in category:
#         if i <= 23:
#             print(item)
#             url = item['href']
#             pagination(url)
#             print('---------------------------------')
#
#             i += 1
#             print('end-----------'+str(i))
#
#
#
# # x = CardProduct.objects.get(url='https://www.littleforbig.com/product/classic-series-black-onesie-bodysuit/')
# find_category(site)
# # product_card_info('https://www.littleforbig.com/product/mad-love-onesie-bodysuit/')
# #  catalog_onesie_bodysuit_skirt_sets('https://www.littleforbig.com/product-category/clothes/adult-onesie-bodysuits/onesie-bodysuit-skirt-sets/')
# # pagination('https://www.littleforbig.com/product-category/clothes/adult-onesie-bodysuits/onesie-bodysuit-skirt-sets/')
#
from parser_site.utils import transliterate

# def trans_sub():
#     all = Subcategory.objects.all()
#
#     for item in all:
#         slug = transliterate(item.name)
#
#         Subcategory.objects.filter(id=item.id).update(name_slug=slug)
# trans_sub()

# def find_category(url):
#     resp = requests.get(url, ua.rand_user_agent())
#     soup = BS(resp.content, 'html.parser')
#     i = 1
#     menu = soup.find('ul', class_='product-categories')
#     category = menu.find_all('a')
#     for item in category:
#         if i <= 23:
#             print(item)
#             url = item['href']
#             pagination(url)
#             print('---------------------------------')
#
#             i += 1
#             print('end-----------'+str(i))
#
# def pagination(url):
#     resp = requests.get(url, ua.rand_user_agent())
#     soup = BS(resp.content, 'html.parser')
#     i = 1
#     path_page = 'page/'
#     count_next_page = soup.find('ul', class_='page-numbers')
#     if count_next_page == None:
#         print(url + path_page + str(i) + '/')
#         catalog_onesie_bodysuit_skirt_sets(url + path_page + str(i) + '/')
#     else:
#         next = count_next_page.find('a', class_='next')
#         while i <= len(count_next_page)-1:
#             print(url + path_page + str(i) + '/')
#             catalog_onesie_bodysuit_skirt_sets(url + path_page + str(i) + '/')
#             i += 1
#
#
# def catalog_onesie_bodysuit_skirt_sets(url):
#     data, errors = [], []
#     resp = requests.get(url, ua.rand_user_agent())
#
#     if resp.status_code == 200:
#         soup = BS(resp.content, 'html.parser')
#         card_vac = soup.find_all('a', class_='woocommerce-LoopProduct-link')
#
#         for div in card_vac:
#             href = div['href']
#             print(href)
#             try:
#                 product_card_info(href)
#             except ValueError:
#                 print('Error')
#     else:
#         errors.append({'url': url, 'text': resp.text})
#
#
#
#


from parser_site.utils import transliterate
#
# def product_card_info(url):
#
#     data, errors = [], []
#     resp = requests.get(url, ua.rand_user_agent())
#     print(resp.status_code)
#     if resp.status_code == 200:
#         soup = BS(resp.content, 'html.parser')
#         translator = google_translator()
#         card_vac = soup.find('div', class_='product-info')
#         # sub = card_vac.find('span', class_='posted_in').text.strip('Categories: ').strip().split(',')
#         sub = card_vac.find('span', class_='posted_in').text
#         import re
#         sub = re.sub(r'Categor\S+', '', sub).strip().split(',')
#
#         for i in sub:
#
#             i  = i.strip()
#             if CardProduct.objects.filter(url=url):
#                 s = CardProduct.objects.get(url=url)
#
#                 if i == 'Onesie Bodysuits':
#                     slug = 'Polzunki_Bodi'
#                 elif i == 'Adult Onesie Bodysuits':
#                     slug = 'Bodi_dlya_vzroslyh'
#                 elif i == 'Onesie Bodysuit Skirt Sets':
#                     slug = 'Polzunkibodi_s_ubkoi'
#                 elif i == 'Lingerie':
#                     slug = 'ZHenskoe_bele'
#                 elif i == 'Corsets':
#                     slug = 'Korsety'
#                 elif i == 'Skirts':
#                     slug = 'Ubki'
#                 elif i == 'Overalls':
#                     slug = 'Kombinezony'
#                 elif i == 'Swimsuit':
#                     slug = 'Kupalniki'
#                 elif i == 'Pajamas':
#                     slug = 'Pizhamy'
#                 elif i == 'Crop top':
#                     slug = 'Ukorochennyi_top'
#                 elif i == 'Jacket':
#                     slug = 'ZHakety'
#                 elif i == 'Coral Fleece Calf Socks':
#                     slug = 'Noski_iz_korallovogo_flisa_'
#                 elif i == 'Fishnet Mesh Net Stockings':
#                     slug = 'Azhurnye_CHulki'
#                 elif i == 'Fuzzy Fleece Lined Slipper Calf Socks':
#                     slug = 'Pushistye_flisovye_tapochki'
#                 elif i == 'Coral Fleece Knee High Socks':
#                     slug = 'Golfy_iz_korallovogo_flisa_'
#                 elif i == 'School Girl Knee High Socks':
#                     slug = 'Golfy_dlya_shkolnic_'
#                 elif i == 'Ankle Cuffs':
#                     slug = 'Manzhety_na_schikolotke'
#                 elif i == 'Collars':
#                     slug = 'Osheiniki'
#                 elif i == 'Luxury Sets':
#                     slug = 'Roskoshnye_nabory'
#                 elif i == 'Wrist Cuffs':
#                     slug = 'Naruchnye_manzhety'
#                 elif i == 'Clothes':
#                     slug = 'Odezda'
#                 elif i == 'Socks':
#                     slug = 'Golfi_'
#                 elif i == 'PrettyInCuffs':
#                     slug = 'naruchniki_i_osheiniki'
#
#
#                 print(slug)
#
#                 if slug != None:
#                     x = Subcategory.objects.get(name_slug=slug)
#
#                     s.subcategory.add(x)
#
#             else:
#                 print('Товара не существует ' + url)
#

def add_cat():
    prettyIncuffs = CardProduct.objects.filter(subcategory__category__name_slug='prettyIncuffs')
    for i in prettyIncuffs:
        x = Subcategory.objects.get(name_slug='prettyIncuffs')
        i.subcategory.add(x)

add_cat()
# # product_card_info('https://www.littleforbig.com/product/heartbreaker-jumperskirt-overall-skirt/')
# # product_card_info('https://www.littleforbig.com/product/usagi-moon-onesie-pink/')
# find_category(site)