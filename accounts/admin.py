from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('アクセス権', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('その他', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )