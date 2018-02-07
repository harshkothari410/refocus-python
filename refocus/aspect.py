"""
	aspect API File
"""
import config
from api import *

class Aspect(object):
	"""docstring for aspect"""
	def __init__(self):
		pass

	def post(self, data):
		"""
		Function for creating aspects using API

		@arguments
			data

		@return
			data of response
		"""
		url = '/aspects'
		return post(url, data)

	def patch(self, data, name=None, id=None):
		"""
		Function for creating aspects using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if name:
			url = '/aspects/' + name
		if id:
			url = '/aspects/' + id

		return patch(url, data)

	def put(self, data, name=None, id=None):
		"""
		Function for creating aspects using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if name:
			url = '/aspects/' + name
		if id:
			url = '/aspects/' + id
			
		return patch(url, data)

	def get(self, name=None, id=None):
		"""
		Function for creating aspects using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if name:
			url = '/aspects/' + name
		elif id:
			url = '/aspects/' + id
                else:
                        url = '/aspects'

		return get(url)

	def delete(self, name=None, id=None):
		"""
		Function for creating aspects using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if name:
			url = '/aspects/' + name
		if id:
			url = '/aspects/' + id

		return delete(url)
