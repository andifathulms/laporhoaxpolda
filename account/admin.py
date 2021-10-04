from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
	list_display = ('email','username', 'office', 'date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username', 'office',)
	readonly_fields=('id', 'date_joined', 'last_login')

	add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email','office','is_admin','is_staff',)}),
    )

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)