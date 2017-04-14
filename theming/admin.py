from django.contrib import admin
from mezzanine.utils.admin import SingletonAdmin
from .models import Bootswatch

class BootswatchAdmin(SingletonAdmin):
	pass

admin.site.register(Bootswatch, BootswatchAdmin)
