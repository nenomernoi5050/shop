from parser_site.models import *


def sub_context_processor(request):
    sub = {
        'clothing': Subcategory.objects.filter(category__name_slug='clothing', view_menu=True).order_by('sorted'),
        'socks': Subcategory.objects.filter(category__name_slug='socks', view_menu=True),
        'prettyIncuffs': Subcategory.objects.filter(category__name_slug='prettyIncuffs', view_menu=True),
    }

    return sub