from django.contrib import admin
from .models import GoodsCategory,Goods,GoodsImage,GoodsCategoryBrand,Banner,IndexAd
import xadmin
# Register your models here.
class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display=['name','add_time']
    list_filter=['category_type','name']
    search_fileds=['name']
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name','category']
    list_filter = ['market_price','name','category']
    search_fileds = ['name']
    style_fields = {"context": "ueditor"}
admin.site.register(GoodsImage)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(GoodsCategoryBrand)
admin.site.register(Banner)
admin.site.register(GoodsCategory,GoodsCategoryAdmin)
admin.site.register(IndexAd)

