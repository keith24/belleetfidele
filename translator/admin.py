from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Translator, Translation

class TranslationAdmin(admin.ModelAdmin):
	pass

admin.site.register(Translator, PageAdmin)
admin.site.register(Translation)
