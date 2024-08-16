from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     fieldsets = (
#         ("Global", {"fields": ("username", "phone_number", "email")}),
#         (
#             "Personal",
#             {
#                 "classes": ("tabular",),
#                 "fields": ("first_name", "last_name", "age", "gender"),
#             },
#         ),
#         (
#             "Permissions",
#             {"fields": ("is_active", "is_staff", "is_superuser", "user_permissions")},
#         ),
#         (
#             "Event Times",
#             {"classes": ("tabular",), "fields": ("last_login", "date_joined")},
#         ),
#     )

#     add_fieldsets = (
#         (
#             "Personal",
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "phone_number", "email", "gender"),
#             },
#         ),
#         (
#             "Security",
#             {
#                 "classes": ("wide",),
#                 "fields": ("password1", "password2"),
#             },
#         ),
#         ("Special Access", {"classes": ("wide",), "fields": ("is_staff",)}),
#     )

#     readonly_fields = ("date_joined", "last_login", "password", "is_superuser")

#     ordering = ("username", "date_joined")
#     filter_horizontal = ("groups", "user_permissions")
#     list_display = (
#         "id",
#         "username",
#         "first_name",
#         "last_name",
#         "last_login",
#         "is_active",
#         "gender",
#         "date_joined",
#     )
#     search_fields = ("id", "email", "first_name", "last_name", "username")
#     list_filter = ("gender", "last_login", "is_active", "date_joined")
#     actions = ["disable_account", "enable_account"]

#     @admin.action(description="Disable users")
#     def disable_account(self, request, queryset):
#         queryset.update(is_active=False)

#     @admin.action(description="Enable users")
#     def enable_account(self, request, queryset):
#         queryset.update(is_active=True)
