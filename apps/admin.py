from django.contrib import admin
from django.apps import apps
from .models import CustomUser
from django.utils.safestring import mark_safe

models = apps.get_app_config('apps').get_models()

@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'username')
    list_display_links = ('username', 'get_image')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="200" height="200" />')
        return mark_safe('<p>No image</p>')


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass