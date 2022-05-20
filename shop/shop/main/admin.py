from django.contrib import admin
from django.utils.html import mark_safe
from .models import Product, Category, Busket, Busketitems, Profile

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'desc', 'image_tag']
    list_filter = ['category']
    search_fields = ['name']

    def image_tag(self, obj):
        return mark_safe('<img src="%s" />' % obj.image.url)

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)


class BusketAdmin(admin.ModelAdmin):
    list_display = ['sessionid']

admin.site.register(Busket, BusketAdmin)

class BusketitemsAdmin(admin.ModelAdmin):
    list_display = ['count', 'product', 'basket']

admin.site.register(Busketitems, BusketitemsAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['phone']

admin.site.register(Profile, ProfileAdmin)