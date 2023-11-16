from django.contrib import admin
from .models import product,Category,Type,cart

# Register your models here.
admin.site.register(product)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(cart)

