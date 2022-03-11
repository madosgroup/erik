from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


admin.site.register(User)
# class CustomUserAdmin(UserAdmin):
#     """Custom User Admin"""
#     list_display = ('likes',
#         'username', 'first_name', 'last_name', 'email', 'is_active', 'language', 'currency', 'host',
#         'is_staff', 'is_superuser', 'email_verified', 'email_secret', 'login_method')
#     list_filter = UserAdmin.list_filter + ('host',)
#     fieldsets = UserAdmin.fieldsets + (
#         (
#             "Custom Profile",
#             {
#                 "fields": (
#                     "profile_picture",
#                     "gender",
#                     "bio",
#                     "birthdate",
#                     "currency",
#                     "language",
#                     "host",
#                     "login_method",
#                 )
#             },
#         ),
#     )
