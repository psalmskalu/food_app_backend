from django.contrib import admin

from accounts.models import User

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone')


admin.site.register(User, AdminUser)