from django.contrib import admin
from .models import BankAccount

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("get_username", "account_number", "is_active")
    list_editable = ("is_active",)
    search_fields = ("user__username", "account_number")

    def get_username(self, obj):
        return obj.user.username
    get_username.admin_order_field = 'user'  # Allows column order sorting
    get_username.short_description = 'Username'  # Renames column head

admin.site.register(BankAccount, BankAccountAdmin)
