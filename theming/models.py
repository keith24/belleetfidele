from django.db import models
import requests

class Bootswatch(models.Model):
	class Meta:
		verbose_name = "Swatch"
		verbose_name_plural = "Swatch"

	# Get themes from Bootswatch.com
	print("\nRetrieving themes from 'https://bootswatch.com/api/3.json'...")
	data = requests.get('https://bootswatch.com/api/3.json').json()
	swatchnames = tuple( (theme['name'],theme['name']) for theme in data['themes'] )
	print("Got {} themes. ".format(len(swatchnames)))

	# Chosen theme
	name = models.CharField( max_length=15, choices=swatchnames, default="Flatly")
