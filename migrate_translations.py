#!/usr/bin/python3
# Keith Irwin
# based on (http://mezzanine.readthedocs.io/en/latest/multi-lingual-sites.html#translation-fields-and-migrations)

import subprocess

default = './mjs/settings.py'

def set_modeltrans(truefalse,filename=default):
	print("Setting USE_MODELTRANSLATION to {}... ".format(truefalse))
	with open(filename,'r') as f:
		lines = f.readlines()
	for l, line in enumerate(lines):
		if line[:20] == "USE_MODELTRANSLATION":
			lines[l] = "USE_MODELTRANSLATION = "+truefalse+"\n"
			#~ break
	with open(filename,'w') as write:
			write.writelines(lines)

# RUNTIME

# edit settings.py to set USE_MODELTRANSLATION = False
set_modeltrans("False")

# migrations
subprocess.run(['python3','manage.py','makemigrations','--noinput'])
subprocess.run(['python3','manage.py','migrate','--noinput'])

# edit settings.py to set USE_MODELTRANSLATION back to True
set_modeltrans("True")

# sync translations
subprocess.run(['python3','manage.py','sync_translation_fields','--noinput'])
