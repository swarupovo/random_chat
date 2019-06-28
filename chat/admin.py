from django.contrib import admin
from django.contrib.auth.models import User

#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('firstname', 'username', 'password', 'email_id')
#     search_fields = ['username']
#     ordering = ['-username']


# admin.site.register(User, UserAdmin)