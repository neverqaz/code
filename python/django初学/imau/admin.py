from django.contrib import admin
from .models import *
# Register your models here.

class BookinfoAdmin(admin.ModelAdmin):
    list_display=['book_name','book_author','book_price','book_house']
    list_filter=['book_price','book_number']
    search_fileds=['book_name','book_author']
admin.site.register(Users1)
admin.site.register(Bookhouse)
admin.site.register(Bookinfo,BookinfoAdmin)
admin.site.register(Booktype)