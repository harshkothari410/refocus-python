"""
	Module for Python Refocus
"""
import requests
import config
import constant
from subject import Subject
from aspect import Aspect
from sample import Sample

class Refocus(object):
	"""docstring for Refocus"""
	def __init__(self, url=None, version=None, token=None):
		self.subject = Subject()
		self.aspect = Aspect()
		self.sample = Sample()

		if url:
			if url.endswith('/'):
				config.REFOCUS_URL = url
			else:
				config.REFOCUS_URL = url + '/'

		if config.API_VERSION or version:
			config.REFOCUS_URL += version if version else config.API_VERSION

		if token:
			config.REFOCUS_TOKEN = token
