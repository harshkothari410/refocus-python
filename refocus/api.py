import requests
import constant
import config
from pprint import pprint
def post(url, data=None):
	"""
	Post request to Refocus for doing perticular work

	@arguments
		data	: data for create / update request, Default = None
		url		: url for request to API

	@return
		data for request
	"""
	try:
		response = requests.post(config.REFOCUS_URL + url, json=data,
			headers={'Authorization': config.REFOCUS_TOKEN})
                if response.status_code == 200 and url == '/samples/upsert/bulk':
                        """
                        unlike every other api call bulk upsert does not return json
                        on success so we need a special case for this
                        """
                        return {'status_code': 200, 'text': response.text}
                else:
                        return response.json()
	except Exception, err:
		return {'errors': [{'message': str(err)}]}

def patch(url, data=None):
	"""
	Patch request to Refocus for doing perticular work

	@arguments
		data	: data for create / update request, Default = None
		url		: url for request to API

	@return
		data for request
	"""
	try:
		response = requests.patch(config.REFOCUS_URL + url, json=data,
			headers={'Authorization': config.REFOCUS_TOKEN})
		return response.json()
	except Exception, err:
		return {'errors': [{'message': str(err)}]}

def get(url):
	"""
	Get request to Refocus for doing perticular work

	@arguments
		data	: data for create / update request, Default = None
		url		: url for request to API

	@return
		data for request
	"""
	try:
		response = requests.get(config.REFOCUS_URL + url,
			headers={'Authorization': config.REFOCUS_TOKEN})
		return response.json()
		# if response.status_code == constant.HTTPSTATUS['OK'] or \
		# 	response.status_code == constant.HTTPSTATUS['CREATED']:
		# 	return response.json()
		# else:
		# 	return response.json()
	except Exception, err:
		return {'errors': [{'message': str(err)}]}

def put(url, data=None):
	"""
	Patch request to Refocus for doing perticular work

	@arguments
		data	: data for create / update request, Default = None
		url		: url for request to API

	@return
		data for request
	"""
	try:
		response = requests.put(config.REFOCUS_URL + url, json=data,
			headers={'Authorization': config.REFOCUS_TOKEN})
		return response.json()
	except Exception, err:
		return {'errors': [{'message': str(err)}]}

def delete(url, data=None):
	"""
	Patch request to Refocus for doing perticular work

	@arguments
		data	: data for create / update request, Default = None
		url		: url for request to API

	@return
		data for request
	"""
	try:
		response = requests.delete(config.REFOCUS_URL + url, json=data,
			headers={'Authorization': config.REFOCUS_TOKEN})
		return response.json()
	except Exception, err:
		return {'errors': [{'message': str(err)}]}
