from django.contrib import admin
from .models import Friend, Belonging, Borrowed


class FriendAdmin(admin.ModelAdmin):
    pass


class BelongingAdmin(admin.ModelAdmin):
    pass


class BorrowedAdmin(admin.ModelAdmin):
    pass


admin.site.register(Friend, FriendAdmin)
admin.site.register(Belonging, BelongingAdmin)
admin.site.register(Borrowed, BorrowedAdmin)
