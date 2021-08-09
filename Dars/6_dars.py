# ikkta tasodifiy son yig'indisini toping

from random import randint

a =  randint(1, 500)
b =  randint(1, 500)

c = int(input('{} + {} = '.format(a, b)))

if c == (a + b):
	print('Togri')
else:
	print('Xato')