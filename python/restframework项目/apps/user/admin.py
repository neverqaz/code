from django.contrib import admin
from .models import VerifyCode,UserProfile
import xadmin
# Register your models here.

class VerifyCodeAdmin(admin.ModelAdmin):
    list_display=['mobile','code','add_time']
    #list_filter=['book_price','book_number']
    #search_fileds=['book_name','book_author']
admin.site.register(VerifyCode,VerifyCodeAdmin)
admin.site.register(UserProfile)
