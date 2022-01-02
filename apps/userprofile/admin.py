from django.contrib import admin

# Register your models here.
from userprofile.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "index",
        "username",
        "email",
        "nickname",
        "status",
        "version",
        "create_time",
        "modify_time",
    )


admin.site.register(Profile, ProfileAdmin)
