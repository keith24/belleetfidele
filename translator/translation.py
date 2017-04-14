from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator as modeltranslator

from .models import Translator

class TranslatedTranslator(TranslationOptions):
	fields = (
		'content',
		'form_title',
		'intro',
		'default_text',
		'langs',
		'quote',
		'buy',
		'too_short',
		'no_email',
		'response_subject',
		'response_body',
		'success_page'
	)

modeltranslator.register(Translator, TranslatedTranslator)
