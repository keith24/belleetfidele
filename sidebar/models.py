from django.db import models
from mezzanine.core.fields import RichTextField

class Sidebar(models.Model):
	class Meta:
		verbose_name = "Sidebar"
		verbose_name_plural = "Sidebar"

	title = models.CharField( max_length=99, default="About" )
	text = RichTextField(default="Gosia is a professional translator")
	imgalt = models.CharField( max_length=222, default="A photo of Gosia" )
