from django.contrib import admin
from .models import Blood

@admin.register(Blood)
class BloodAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_blood_group', 'last_donate_date')
    search_fields = ('user__username', 'person__blood_group')
    list_filter = ('person__blood_group',)

    def get_blood_group(self, obj):
        return obj.person.blood_group if obj.person else "N/A"
    get_blood_group.short_description = 'Blood Group'
