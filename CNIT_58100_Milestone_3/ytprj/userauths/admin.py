from django.contrib import admin

# Register your models here.
from userauths.models import User

from import_export.admin import ImportExportModelAdmin

class UserAdmin(ImportExportModelAdmin):
    pass

admin.site.register(User,UserAdmin)
