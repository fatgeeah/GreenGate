from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(FeedBack)
admin.site.register(Reply)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
