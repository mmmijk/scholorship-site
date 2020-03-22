from django.contrib import admin

from .models import rise

# Register your models here.
@admin.register(rise)
class RizeAdmin(admin.ModelAdmin):
    list_display = ("title","href","intro","status","solve","created_time")
    fields = ("title","href","intro")
    