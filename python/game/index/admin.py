from django.contrib import admin
import xadmin
# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
from xadmin import views
class edit(object):
    site_title='绝地求生博客管理'
    site_footer = "阳澄湖捉螃蟹"
    menu_style = "accordion"
class BaseSetting(object):
    enable_themes =True
    use_bootswatch =True
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,edit)
class ArticleAdmin(object):
    style_fields = {"context": "ueditor"}
    list_display=['aid','title','category','author','go_to']
    list_filter=['category','title','author']
    list_editable = ['title','author','context','category','createtime']
    search_fileds=['aid','category']
class CommentAdmin(object):
    list_display=['cid','email','createtime','message','go_to']
    list_filter=['cid','createtime',]
    search_fileds=['cid','createtime']
    list_editable = ['email', 'message']
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Comment,CommentAdmin)