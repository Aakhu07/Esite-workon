from django.contrib import admin
from .models import *

admin.site.register(Ad)
admin.site.register(Brand)
admin.site.register(Slider)
admin.site.register([Customer,Category,Product,Cart,CartProduct,Order,Admin])
