from django.contrib import admin

from .models import Transaction, VirtualAccount

admin.site.register(Transaction)
admin.site.register(VirtualAccount)