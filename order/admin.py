from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at')

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Contact)
admin.site.register(FeedBack)

# Register your models here.