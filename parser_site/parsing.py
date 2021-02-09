import requests
import codecs
from bs4 import BeautifulSoup as BS
import csv
from parser_site.models import *
import parser_site.user_agent_list as ua
from google_trans_new import google_translator


site = 'https://www.littleforbig.com/product-category/clothes/'




def pagination(url):
    resp = requests.get(url, ua.rand_user_agent())
    soup = BS(resp.content, 'html.parser')
    i = 1
    path_page = 'page/'
    count_next_page = soup.find('ul', class_='page-numbers')
    if count_next_page == None:
        print(url + path_page + str(i) + '/')
        catalog_onesie_bodysuit_skirt_sets(url + path_page + str(i) + '/')
    else:
        next = count_next_page.find('a', class_='next')
        while i <= len(count_next_page)-1:
            print(url + path_page + str(i) + '/')
            catalog_onesie_bodysuit_skirt_sets(url + path_page + str(i) + '/')
            i += 1


def catalog_onesie_bodysuit_skirt_sets(url):
    data, errors = [], []
    resp = requests.get(url, ua.rand_user_agent())

    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        card_vac = soup.find_all('a', class_='woocommerce-LoopProduct-link')

        for div in card_vac:
            href = div['href']
            print(href)
            try:
                if CardProduct.objects.filter(url=href):
                    print('Существует')
                else:
                    product_card_info(href)
            except ValueError:
                print('Error')
    else:
        errors.append({'url': url, 'text': resp.text})


    with open ('../littleforbig.csv', 'w', newline ='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)

    h = codecs.open('../error_littleforbig.txt', 'w', 'utf-8')
    h.write(str(errors))
    h.close()

def product_card_foto(url):
    path = 'media/images/images-card/'
    data = []
    errors = []

    resp = requests.get(url, ua.rand_user_agent())
    print(resp.status_code)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        card_img = soup.find('div', class_='product-thumbnails')
        card_vac = card_img.find_all('div', class_='col')

        for div in card_vac:
            image_thumb = div.find('img', class_='attachment-woocommerce_thumbnail')

            if None in image_thumb.get_attribute_list('data-src'):
                photo_url = image_thumb.get_attribute_list('src')[0]
            else:
                photo_url = image_thumb.get_attribute_list('data-src')[0]


            save_data(path, get_name(photo_url), get_file(photo_url))

            data.append(path + get_name(photo_url))

        return data


    else:
        errors.append({'url': url, 'text': resp.text})
    h = codecs.open('../error_littleforbig.txt', 'w', 'utf-8')
    h.write(str(errors))
    h.close()


def product_card_info(url):
    dollar = 100
    path = 'media/images/images-card/'
    data,errors = [], []
    resp = requests.get(url, ua.rand_user_agent())
    print(resp.status_code)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        translator = google_translator()
        breadcump_cat = translator.translate(((soup.find('nav', class_='woocommerce-breadcrumb').find_all('a')[1].get_text()).title()), lang_tgt='ru')
        breadcump_subcat = translator.translate(((soup.find('nav', class_='woocommerce-breadcrumb').find_all('a')[-1].get_text()).title()), lang_tgt='ru')

        card_vac = soup.find('div', class_='product-info')
        title = card_vac.find('h1', class_='product-title').text.strip()
        price = round(float(card_vac.find('bdi').text[1:])) * dollar
        if soup.find('td', class_='woocommerce-product-attributes-item__value') == None:
            size = None
        else:
            size = soup.find('td', class_='woocommerce-product-attributes-item__value').text

        desc_one = soup.find('div', id='tab-description').text.strip('\n')
        import re
        desc_one = re.sub(r'http\S+', '', desc_one)
        i = desc_one.rfind('Related Post on Instagram')
        if i != -1:
            desc_one = desc_one[:i]
        desc_one = translator.translate(desc_one, lang_tgt='ru')
        Category.objects.get_or_create(name=breadcump_cat, name_slug=(translator.translate(breadcump_cat, lang_tgt='en')).strip().replace(" ", "_"))
        c = Category.objects.get(name=breadcump_cat)
        Subcategory.objects.get_or_create(name=breadcump_subcat, name_slug=(translator.translate(breadcump_subcat, lang_tgt='en').strip().replace(" ", "_")), category=c)
        sub = Subcategory.objects.get(name=breadcump_subcat)
        # Качаем фотки
        img_name = product_card_foto(url)

        data.append({'title': title,
                     'url': url,
                     'price': price,
                     'size': size,
                     'desc_one': desc_one,
                      })

        s = CardProduct(title=title, url=url, price=price, size=size, desc_one=desc_one, subcategory=sub)

        try:
            s.save()
            for i in img_name:
                pic = CardFoto()
                pic.product = s
                pic.image = i
                pic.save()
        except ValueError:
            print('Error save')

    else:
        errors.append({'url': url, 'text': resp.text})



    return data, errors





def parse_instagramm(url):
    resp = requests.get(url, ua.rand_user_agent())
    print(resp.status_code)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        card_vac = soup.find('img', class_='FFVAD')
        return card_vac['src']


def get_file(url):
    response = requests.get(url, stream=True)
    return response


def save_data(path, name, file_data):
    file = open(path + name, 'bw') #Бинарный режим, изображение передається байтами
    for chunk in file_data.iter_content(4096): # Записываем в файл по блочно данные
        file.write(chunk)


def get_name(url):
    name = url.split('/')[-1]
    return name

def get_name_category(url):
    name = url.split('/')[-2]
    return name



def find_category(url):
    resp = requests.get(url, ua.rand_user_agent())
    soup = BS(resp.content, 'html.parser')
    i = 1
    menu = soup.find('ul', class_='product-categories')
    category = menu.find_all('a')
    for item in category:
        if i <= 23:
            print(item)
            url = item['href']
            pagination(url)
            print('---------------------------------')

            i += 1
            print('end-----------'+str(i))

# ###############Парсинг нового товара если такой вылез при обновлении информации ############
# ############                   ################
list_new_product = [
    'https://www.littleforbig.com/product/cute-animal-coral-fleece-thigh-high-socks-2-pack-sheep-pink-panda-blue/',
]

def new_poduct(list):
    for item in list_new_product:
        product_card_info(item)
        print(item)



# find_category(site)

# product_card_info('https://www.littleforbig.com/product/cute-animal-coral-fleece-thigh-high-socks-2-pack-sheep-pink-panda-blue/')
#  catalog_onesie_bodysuit_skirt_sets('https://www.littleforbig.com/product-category/clothes/adult-onesie-bodysuits/onesie-bodysuit-skirt-sets/')
# pagination('https://www.littleforbig.com/product-category/clothes/adult-onesie-bodysuits/onesie-bodysuit-skirt-sets/')
