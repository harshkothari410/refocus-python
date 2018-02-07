"""
	Samples API File
"""
import config
from api import *

class Sample(object):
	"""docstring for aspect"""
	def __init__(self):
		pass

	def post(self, data):
		"""
		Function for creating samples using API

		@arguments
			data

		@return
			data of response
		"""
		url = '/samples'
		return post(url, data)

	def patch(self, data, name=None, id=None):
		"""
		Function to update sample using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if name:
			url = '/samples/' + name
		if id:
			url = '/samples/' + id

		return patch(url, data)

	def upsert(self, data):
		"""
		Function for upserting samples using API

		@arguments 
			data

		@return
			data of response
		"""
		url = '/samples/upsert'
		return post(url, data)

        def upsert_bulk(self, data):
                """
		Function for bulk upserting samples using API

		@arguments 
			data

		@return
			data of response
		"""
                url = '/samples/upsert/bulk'
                return post(url, data)

	def delete(self, name=None, id=None):
		"""
		Function for creating samples using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if name:
			url = '/samples/' + name
		if id:
			url = '/samples/' + id

		return delete(url)

	def get(self, name=None, id=None):
		"""
		Function to get samples using API

		@arguments
			name: name of sample
			id: id of sample

		@return
			data of response
		"""
		url = ''
		if name:
			url = '/samples/' + name
		elif id:
			url = '/samples/' + id
		else:
			url = '/samples'

		return get(url)
