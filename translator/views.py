#~ from django.shortcuts import render
from datetime import datetime
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseServerError
from .models import Translator
from .models import Translation
import stripe

def translate(req):
	"""
	User requests a translation, and pays
	"""

	translator_page = Translator.objects.first()
	stripe.api_key = translator_page.stripe_sk
	
	if req.method == 'POST':
		
		# Confirm payment w/stripe
		try:
			confirmed_token = stripe.Token.retrieve(req.POST['token'])
		except stripe.error.InvalidRequestError:
			print('ERROR: Unable to confirm token. ')
			return HttpResponse('Stripe token not found')

		# Create new translation object and store to database
		translation = Translation()
		translation.email = req.POST['email']
		translation.words = req.POST['words']
		translation.cost = req.POST['cost']
		translation.days = req.POST['days']
		translation.lang = req.POST['lang']
		translation.text = req.POST['text']
		translation.currency = req.POST['currency']
		translation.locale = req.POST['locale']
		translation.submitted = datetime.now()
		try:
			translation.stripe_token = confirmed_token['id']
			translation.zip_code = confirmed_token['card']['address_zip']
			translation.country = confirmed_token['card']['country']
			translation.ip_address = confirmed_token['client_ip']
			translation.credit_card_ending = confirmed_token['card']['last4']
			translation.submitted = confirmed_token['created']
		except:
			translation.stripe_token = "UNCONFIRMED: "+req.POST['token']
			print("ERROR: Unable to get data from token confirmation response. ")

		translation.save()

		# Send email to user with same information
		email_content = translator_page.response_body\
			.replace('{$words$}',translation.words)\
			.replace('{$cost$}',translation.cost)\
			.replace('{$days$}',translation.days)\
			.replace('{$lang$}',translation.lang)\
			.replace('{$id$}',translation.stripe_token[4:])
		send_mail(
			subject = translator_page.response_subject\
				.replace('{$words$}',translation.words)\
				.replace('{$cost$}',translation.cost)\
				.replace('{$days$}',translation.days)\
				.replace('{$lang$}',translation.lang)\
				.replace('{$id$}',translation.stripe_token[4:]),
			message = email_content,
			html_message = email_content,
			from_email = "gosia@belleetfidele.com",
			recipient_list = [translation.email]
		)
		
		# Send email to Gosia
		send_mail(
			subject = "MJS[{}]: Translate {} words to {}, in {} days for {} {} ({})".format(
				translation.locale,
				translation.words,
				translation.lang,
				translation.days,
				translation.cost,
				translation.currency,
				translation.stripe_token[4:]
			),
			message = translation.text,
			from_email = translation.email,
			recipient_list = ['gosia@belleetfidele.com']
		)

		return HttpResponse(translator_page.success_page)
