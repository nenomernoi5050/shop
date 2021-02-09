from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CardProduct, CardFoto, Subcategory, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ShopShotsInline(admin.TabularInline):
    model = CardFoto
    extra = 0
    readonly_fields = ('get_image',)


    def get_image(self, obj):

        return mark_safe(f'<img src="/{obj.image}" width="120"')

    get_image.short_description = "Изображение"

class CardProductAdminForm(forms.ModelForm):
    desc_one = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = CardProduct
        fields = '__all__'



@admin.register(CardProduct)
class CardProductAdmin(admin.ModelAdmin):
    form = CardProductAdminForm
    inlines = [ShopShotsInline]
    list_display = ('title', 'get_sub_cat', 'price',)
    save_on_top = True
    list_max_show_all = 50



# admin.site.register(CardProduct)
@admin.register(CardFoto)
class CardFotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'get_image')
    readonly_fields = ('get_image',)
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="/{obj.image}" width="120"')

    get_image.short_description = "Изображение"


# admin.site.register(CardFoto)
admin.site.register(Category)
admin.site.register(Subcategory)




admin.site.site_title = 'Администрирование магазина'
admin.site.site_header = 'Администрирование магазина'
admin.site.site_color = 'red'