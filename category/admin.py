from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    #con esto se llena automaticamente el slug, con el valor category_name
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug')

admin.site.register(Category,CategoryAdmin)
