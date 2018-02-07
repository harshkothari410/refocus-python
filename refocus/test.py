from Refocus import Refocus
from pprint import pprint
import config
s = Refocus()

print s
print s.subject.delete_tag(subject_id='227278a9-d528-4c40-a2bf-76d4862dabb8')
# data = {
# 	'name' : 'www12341',
# 	# 'absolutePath' : '',
# }

# # print dir(s.subject)
# x = s.subject.post(data)
# print x
# print s.subject.get(absolute_path='www12341')

# name = 'example'
# data = {
# 	'name' : 'hello'
# }
# response = s.subject.patch(data, absolute_path=name)
# print response
# pprint (x)
# print config.REFOCUS_URL
# x = s.subject.delete(id='1')
# pprint(x)
# x = s.get_subject(id='eu')
# print x

# pprint (x)
# id = '8fe683cb-d32f-4c15-8dc6-52b6f13c5b17'

# data = {
# 	'name' : 'test_subject_1',
# }

# print s.patch_subject(id, data)

