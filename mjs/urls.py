from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.i18n import set_language
from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings
from mezzanine.pages.views import page
#from mezzanine.blog.views import blog_post_list
# from cartridge.shop.views import order_history

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = i18n_patterns(
	# Change the admin prefix here to use an alternate URL for the
	# admin interface, which would be marginally more secure.
	url("^admin/", include(admin.site.urls)),
)

if settings.USE_MODELTRANSLATION:
	urlpatterns += [
		url('^i18n/$', set_language, name='set_language'),
	]

urlpatterns += [

	# Cartridge URLs.
	#url("^shop/", include("cartridge.shop.urls")),
	#url("^account/orders/$", order_history, name="shop_order_history"),

	# HOMEPAGE
	# --------
	# Static template
	#url("^$", direct_to_template, {"template": "pages/index.html"}, name="home"),
	# Editable rich text page
	url("^$", page, {"slug":"/"}, name="home"),
	# Blog-only
	#url("^$", blog_post_list, name="home"),

	# CUSTOM APPS
	# -----------
	# IMPORT APPS' URLS.PY HERE IF NEEDED
	# Translator
	url(r'^translate/', include('translator.urls')),

	# MEZZANINE'S URLS
	# ----------------
	# ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
	# ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
	# FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
	# WILL NEVER BE MATCHED!

	# If you'd like more granular control over the patterns in
	# ``mezzanine.urls``, go right ahead and take the parts you want
	# from it, and use them directly below instead of using
	# ``mezzanine.urls``.
	url("^", include("mezzanine.urls")),

	# MOUNTING MEZZANINE UNDER A PREFIX
	# ---------------------------------
	# You can also mount all of Mezzanine's urlpatterns under a
	# URL prefix if desired. When doing this, you need to define the
	# ``SITE_PREFIX`` setting, which will contain the prefix. Eg:
	# SITE_PREFIX = "my/site/prefix"
	# For convenience, and to avoid repeating the prefix, use the
	# commented out pattern below (commenting out the one above of course)
	# which will make use of the ``SITE_PREFIX`` setting. Make sure to
	# add the import ``from django.conf import settings`` to the top
	# of this file as well.
	# Note that for any of the various homepage patterns above, you'll
	# need to use the ``SITE_PREFIX`` setting as well.

	# url("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls"))

]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
