import sys, os
sys.path.insert(0, os.path.abspath('..'))

from refocus import Refocus
r = Refocus()

def test_post_success_sample():

	data = {
		'name' : 'test_subject',
		'isPublished' : True
	}
	subject = r.subject.post(data)
	subjectId = subject['id']
	name = 'example'
	data = {
		'name' : 'test_aspect',
		'timeout' : '0m',
		'isPublished' : True
	}

	aspect = r.aspect.post(data)
	aspectId = aspect['id']

	print subjectId, aspectId
	data = {
		'name' : name,
		'subjectId' : subjectId,
		'aspectId' : aspectId
	}

	response = r.sample.post(data)
	print response
	assert response['name'], 'test_subject|test_aspect'

def test_post_fail_sample():
	name = 'example'
	data = {
		'name' : name
	}
	response = r.sample.post(data)
	assert len(response['errors']) > 0, True

def test_get_all_success_sample():
	response = r.sample.get()
	print response
	assert response[0]['name'], 'test_subject|test_aspect'

def test_get_success_sample():
	name = 'test_subject|test_aspect'
	response = r.sample.get(name=name)
	print response
	assert response['name'], name

def test_get_fail_sample():
	name = 'example1'	
	response = r.sample.get(name=name)
	assert len(response['errors']) > 0, True

def test_patch_success_sample():
	name = 'test_subject|test_aspect'
	data = {
		 'relatedLinks': [{ 'name': 'xyz', 'url': 'http://xyz.com'}]
	}
	response = r.sample.patch(data, name=name)
	assert response['relatedLinks'][0]['url'], 'http://xyz.com'

def test_patch_fail_sample():
	name = 'example1'
	data = {
		'name' : 'hello'
	}
	response = r.sample.patch(data, name=name)
	assert len(response['errors']) > 0, True

def test_delete_success_sample():
	name = 'test_subject|test_aspect'
	response = r.sample.delete(name=name)
	assert response['name'], name

def test_delete_fail_sample():
	name = 'example1'
	response = r.sample.delete(name=name)
	assert len(response['errors']) > 0, True

def test_upsert_success_sample():
	data = {
		'name' : 'test_subject|test_aspect'
	}
	response = r.sample.upsert(data)
	assert response['name'], 'test_subject|test_aspect'
	response = r.sample.delete(name=data['name'])

def test_upsesrt_fail_sample():
	data = {
		'name' : 'example1'
	}
	response = r.sample.upsert(data)
	assert len(response['errors']) > 0, True
	r.subject.delete(absolute_path='test_subject')
	r.aspect.delete(name='test_aspect')