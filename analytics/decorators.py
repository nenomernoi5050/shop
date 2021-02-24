from functools import wraps
from django.db.models import F
from django.db import transaction
from parser_site.models import *
from .models import PageHit


def counted(f):
    @wraps(f)
    def decorator(request, *args, **kwargs):
        try:
            with transaction.atomic():
                x = kwargs.get("slug")
                print(x)

                product = CardProduct.objects.get(slug=x)
                print(product)
                counter, created = PageHit.objects.get_or_create(product=product)
                counter.count = F('count') + 1
                counter.save()
        except:
            pass
        return f(request, *args, **kwargs)

    return decorator
