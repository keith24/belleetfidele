from django.db import models
from decimal import Decimal
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField

class Translation(models.Model):
	"""
	A requested translation, stored in the database as a backup.
	"""
	def __str__(self):
		return self.stripe_token
	
	lang = models.CharField( max_length=22, default='English' )
	text = models.TextField( default="" )
	words = models.IntegerField( default=0 )
	cost = models.DecimalField( decimal_places=2, max_digits=8, default=Decimal('0.00') )
	currency = models.CharField( max_length=3, default='EUR' )
	ip_address = models.GenericIPAddressField( default='0.0.0.0' )
	zip_code = models.IntegerField( default=12345 )
	country = models.CharField( max_length=2, default='ES' )
	locale = models.CharField( max_length=6, default='en' )
	submitted = models.DateTimeField(auto_now_add=True)
	days = models.IntegerField( default=1 )
	email = models.EmailField( default='default@example.com' )
	stripe_token = models.CharField( max_length=30, default='' )
	credit_card_ending = models.CharField( max_length=4, default='0000' )

class Translator(Page):
	"""
	The homepage with translation form
	"""
	class Meta:
		verbose_name = "Translator"
		verbose_name_plural = "Translator"
	
	content = RichTextField( default="An introduction to human translations..." )
	form_title = models.CharField( max_length=40, default="Quick Translation" )
	intro = models.TextField( default="Enter a block of text in the field below to get a quote. " )
	default_text = models.TextField( default="Lorem ipsum..." )
	langs = models.CharField( max_length=100, default='English,Polish,German,Spanish' )
	quote = models.TextField( default="These {$words()$} words will be translated "+
		"from <from-lang></from-lang> "+
		"to <to-lang></to-lang> "+
		"in {$days()$} days and "+
		"emailed to <input-email></input-email>.")
	buy = models.CharField( max_length=160, default='Buy translation for ${$cost()$}' )
	too_short = models.CharField( max_length=99, default='Please enter at least {$min_words()$} words' )
	no_email = models.CharField( max_length=99, default='Please enter a valid email address' )
	price_word = models.DecimalField( decimal_places=5, max_digits=7, default=Decimal('.035') )
	words_day = models.IntegerField( default=3000 )
	min_words = models.IntegerField( default=100 )
	stripe_pk = models.CharField( max_length=32, default='pk_test_MRewRKR8aCk7Nai6howeJF4E' )
	stripe_sk = models.CharField( max_length=32, default='sk_test_wtXqu7ulh7MLKSfzGgCs9vKv' )
	response_subject = models.CharField( max_length=555, default='Thank you!' )
	response_body = RichTextField( default="We have received your text and will translate it as soon as possible." )
	success_page = RichTextField( default="We have received your text and will translate it as soon as possible." )
