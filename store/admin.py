from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    ##lo que queremos listar
    list_display = ('product_name','price','stock','category','modified_date','is_available')
    #lo que quiero autollenar
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product,ProductAdmin)
