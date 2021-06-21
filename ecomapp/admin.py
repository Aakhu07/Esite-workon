from django.contrib import admin
from .models import *

admin.site.register(Ad)
admin.site.register([Customer,Category,Product,Cart,CartProduct,Order])
