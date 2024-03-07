# -*- coding: UTF-8 -*-
"""
	Add-On for test with github an so on 
	Author: Rainer Brell
"""

import addonHandler
import globalPluginHandler
from scriptHandler import script

addonHandler.initTranslation()

def myStatistic():
	"""
		This is only a temprorary test 
	""" 
	import urllib 
	import os 
	import addonHandler
	import languageHandler 
	import datetime 
	from versionInfo import version as nvdaVersion 
	addonName    = "pressed"
	addonVersion = "0"
	lang         = languageHandler.getLanguage().lower()
	fileName     = (addonName + addonVersion + ".csv")
	date         = datetime.datetime.now().strftime("%Y.%m.%d")
	time         = datetime.datetime.now().strftime("%H:%M:%S")
	line         = lang + ";" + nvdaVersion + ";" + date + ";" + time 
	base_url = "https://nvda.brell.net/statistic"
	params = {
		"param1": fileName,
		"param2": line
	}
	url = f"{base_url}?fileName={params['param1']}&line={params['param2']}"
	try: 
		urllib.request.urlopen(url)
	except:
		pass

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: Script Category
	scriptCategory = _("My Mouse")

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)

	@script(
		description="Here comes the mouse",
		gesture="kb:NVDA+control+0"
	)
	def script_xMouse(self, gesture):
		import ui
		myStatistic()
		# Translators: Message for test 
		ui.message(_("Here comes the mouse"))
