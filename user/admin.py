from django.contrib import admin
from .models import ExpUser
from django.contrib.auth.admin import UserAdmin

class ExpUserAdmin(UserAdmin):
    list_display = ("username","email","is_admin","is_staff","last_login_date","signing_date")
    search_fields = ("email","username")
    readonly_fields = ("signing_date","last_login_date")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ExpUser , ExpUserAdmin)