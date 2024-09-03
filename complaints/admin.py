from django.contrib import admin
from .models import Complaint
from django.utils.html import format_html


class CustomComplaintAdmin(admin.ModelAdmin):
    model = Complaint
    list_display = ('user', 'type_of_complaint', 'created_at', 'action_taken', 'image_tag')
    list_filter = ('type_of_complaint', 'action_taken')
    search_fields = ('type_of_complaint', 'description')
    ordering = ('-created_at',)
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        else:
            return '-'
    image_tag.short_description = 'Image'
    
    
admin.site.register(Complaint, CustomComplaintAdmin)