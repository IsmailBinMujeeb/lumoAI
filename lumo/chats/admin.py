from django.contrib import admin
from .models import chat, message


class chat_admin(admin.ModelAdmin):
    model = chat


admin.site.register(chat, chat_admin)
admin.site.register(message)
