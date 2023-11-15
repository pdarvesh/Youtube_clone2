from django.contrib import admin
from channel.models import Channel
from import_export.admin import ImportExportModelAdmin

class ChannelAdmin(ImportExportModelAdmin):
    list_display = ["channel_name", "user" ,"status"]

admin.site.register(Channel, ChannelAdmin)

# class CommunityAdmin(ImportExportModelAdmin):
#     list_display = ["channel","status"]

# class CommunityCommentAdmin(ImportExportModelAdmin):
#     list_display = ["user", "comment"]



# admin.site.register(Community, CommunityAdmin)
# admin.site.register(CommunityComment, CommunityCommentAdmin)