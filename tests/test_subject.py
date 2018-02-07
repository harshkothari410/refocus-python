import sys, os
sys.path.insert(0, os.path.abspath('..'))

from refocus import Refocus
r = Refocus()

def test_post_success_subject():
	name = 'example'
	data = {
		'name' : name
	}
	response = r.subject.post(data)
	assert response['name'], name

def test_post_fail_subject():
	name = 'example'
	data = {
		'name' : name
	}
	response = r.subject.post(data)
	assert len(response['errors']) > 0, True

def test_get_success_subject():
	name = 'example'
	response = r.subject.get(absolute_path=name)
	print response
	assert response['name'], name

def test_get_fail_subject():
	name = 'example1'	
	response = r.subject.get(absolute_path=name)
	assert len(response['errors']) > 0, True

def test_patch_success_subject():
	name = 'example'
	data = {
		'name' : 'hello'
	}
	response = r.subject.patch(data, absolute_path=name)
	print response
	assert response['name'], 'hello'

def test_patch_fail_subject():
	name = 'example1'
	data = {
		'name' : 'hello'
	}	
	response = r.subject.patch(data, absolute_path=name)
	assert len(response['errors']) > 0, True

def test_put_success_subject():
	name = 'hello'
	response = r.subject.post({
		'name': 'hello',
		'isPublished': True
	})
	data = {
		'name' : 'example'
	}
	response = r.subject.put(data, absolute_path=name)
	print response
	assert response['name'], 'example'

def test_put_fail_subject():
	name = 'example1'
	data = {
		'name' : 'hello'
	}	
	response = r.subject.put(data, absolute_path=name)
	assert len(response['errors']) > 0, True

def test_delete_success_subject():
	name = 'example'
	response = r.subject.delete(absolute_path=name)
	assert response['name'], name

def test_delete_fail_subject():
	name = 'example1'
	response = r.subject.delete(absolute_path=name)
	assert len(response['errors']) > 0, True

def test_get_hierarchy_subject():
	r.subject.post({
		'name': 'parent',
		'isPublished': True
	})
	r.subject.post({
		'name': 'child',
		'parentAbsolutePath': 'parent',
		'isPublished': True
	})
	print r.subject.post({
		'name': 'grand_child',
		'parentAbsolutePath': 'parent.child',
		'isPublished': True,
		'tags': [ 'Datacenter''Ashburn-ASG' ]
	})
	response = r.subject.get_hierarchy(absolute_path='parent.child')
	print response
	assert response['name'], 'child'
	assert response['children'][0]['name'], 'grand_child'

def test_fail_hierarchy_subject():
	response = r.subject.get_hierarchy(absolute_path='parent.child1')
	assert len(response['errors']) > 0, True