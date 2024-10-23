from django.contrib import admin
from .models import CustomsUser


@admin.register(CustomsUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'avatar','phone_number')
    list_filter = ('country',)
    search_fields = ('email',)
