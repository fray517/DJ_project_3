from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Административная панель для кастомной модели пользователя."""

    list_display = ("username", "email", "phone_number", "is_staff", "date_joined")
    list_filter = ("is_staff", "is_superuser", "is_active", "date_joined")
    search_fields = ("username", "email", "phone_number")
    ordering = ("-date_joined",)

    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {
            "fields": ("phone_number",)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Дополнительная информация", {
            "fields": ("email", "phone_number")
        }),
    )
