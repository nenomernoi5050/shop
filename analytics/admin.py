from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import PageHit
from parser_site.models import *



@admin.register(PageHit)
class PostAdmin(admin.ModelAdmin):

    list_display = ('product', 'count')

    def has_add_permission(self, request):
        return False

# @admin.register(PageHit)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('product', 'get_image', 'count',)
#     readonly_fields = ('get_image', 'count')
#     save_on_top = True
#
#     def has_add_permission(self, request):
#         return False
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src="/{obj.image}" width="120"')
#
#     get_image.short_description = "Изображение"