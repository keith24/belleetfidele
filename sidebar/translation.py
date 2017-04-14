from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator as modeltranslator

from .models import Sidebar

class TranslatedSidebar(TranslationOptions):
	fields = ('title','text','imgalt')

modeltranslator.register(Sidebar, TranslatedSidebar)
