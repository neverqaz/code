from django.contrib import admin
from .models import UserAli,UserAddress,UserLeavingMessage,AlipayOrderSettle
# Register your models here.
admin.site.register(UserLeavingMessage)
admin.site.register(UserAddress)
admin.site.register(UserAli)
admin.site.register(AlipayOrderSettle)
