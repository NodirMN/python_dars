from random import randint
yangi_kod = randint(130, 135)
kodlar = [135, 132, 134, 131] # list
yangi_kod = randint(130, 135)

i = 0
while yangi_kod in kodlar:
	i += 1
	yangi_kod = randint(130, 135)

print('Takrorlanishlar soni: ', i)
print(yangi_kod)