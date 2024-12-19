from django.contrib import admin

from .models import Visits, Visitor

# Register your models here.
@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
    list_display = ('count',)

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'visit_time')
