from django.contrib import admin
from mezzanine.utils.admin import SingletonAdmin
from .models import Sidebar

class SidebarAdmin(SingletonAdmin):
	pass

admin.site.register(Sidebar, SidebarAdmin)
