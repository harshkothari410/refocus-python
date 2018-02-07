"""
	Subject API File
"""
import config
from api import *

class Subject(object):
	"""docstring for Subject"""
	def __init__(self):
		pass

	def post(self, data):
		"""
		Function for creating subjects using API

		@arguments
			data

		@return
			data of response
		"""
		url = '/subjects'
		return post(url, data)

	def patch(self, data, absolute_path=None, id=None):
		"""
		Function for creating subjects using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if absolute_path:
			url = '/subjects/' + absolute_path
		if id:
			url = '/subjects/' + id

		return patch(url, data)

	def put(self, data, absolute_path=None, id=None):
		"""
		Function for creating subjects using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if absolute_path:
			url = '/subjects/' + absolute_path
		if id:
			url = '/subjects/' + id
			
		return put(url, data)

	def get(self, absolute_path=None, id=None):
		"""
		Function for creating subjects using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if absolute_path:
			url = '/subjects/' + absolute_path
		elif id:
			url = '/subjects/' + id
                else:
                        url = '/subjects'

		return get(url)

	def get_hierarchy(self, absolute_path=None, id=None):
		"""
		Function to get subject hierarchy using API

		@arguments
			absolute_path: absolute path of subject
			id: id of subject

		@return
			data of response
		"""
		url = ''
		if absolute_path:
			url = '/subjects/' + absolute_path + '/hierarchy'
		if id:
			url = '/subjects/' + id + '/hierarchy'

		return get(url)

	def delete(self, absolute_path=None, id=None):
		"""
		Function for creating subjects using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''
		if absolute_path:
			url = '/subjects/' + absolute_path
		if id:
			url = '/subjects/' + id

		return delete(url)

	def delete_tag(self, id=None, absolute_path=None, subject_id=None):
		"""
		Function for deleting subjects tags using API

		@arguments
			data

		@return
			data of response
		"""
		url = ''

		if absolute_path:
			url = '/subjects/' + absolute_path + '/tags/'
		if subject_id:
			url = '/subjects/' + subject_id + '/tags/'
		if id:
			url += id

		return delete(url)

