import sys, os
sys.path.insert(0, os.path.abspath('..'))

from refocus import Refocus
r = Refocus()

def test_post_success_aspect():
	name = 'example'
	data = {
		'name' : name,
		'timeout' : '0m'
	}
	response = r.aspect.post(data)
	print response
	assert response['name'], name

def test_post_fail_aspect():
	name = 'example'
	data = {
		'name' : name
	}
	response = r.aspect.post(data)
	assert len(response['errors']) > 0, True

def test_get_success_aspect():
	name = 'example'
	response = r.aspect.get(name=name)
	assert response['name'], name

def test_get_fail_aspect():
	name = 'example1'	
	response = r.aspect.get(name=name)
	assert len(response['errors']) > 0, True

def test_patch_success_aspect():
	name = 'example'
	data = {
		'name' : 'hello'
	}
	response = r.aspect.patch(data, name=name)
	assert response['name'], 'hello'

def test_patch_fail_aspect():
	name = 'example1'
	data = {
		'name' : 'hello'
	}	
	response = r.aspect.patch(data, name=name)
	assert len(response['errors']) > 0, True

def test_put_success_aspect():
	name = 'hello'
	data = {
		'name' : 'example'
	}
	response = r.aspect.put(data, name=name)
	assert response['name'], 'example'

def test_put_fail_aspect():
	name = 'example1'
	data = {
		'name' : 'hello'
	}	
	response = r.aspect.put(data, name=name)
	assert len(response['errors']) > 0, True

def test_delete_success_aspect():
	name = 'example'
	response = r.aspect.delete(name=name)
	assert response['name'], name

def test_delete_fail_aspect():
	name = 'example1'
	response = r.aspect.delete(name=name)
	assert len(response['errors']) > 0, True
