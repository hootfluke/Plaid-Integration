from django.contrib import admin
from .models import plaidUser

class plaidUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'token', 'access_token')

admin.site.register(plaidUser, plaidUserAdmin)