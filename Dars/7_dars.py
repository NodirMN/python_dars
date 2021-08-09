summa = input('Summani kiriting:')

if summa.isdigit() and int(summa) > 0 and int(summa) < 1000000:
	print('Tashakur')
else:
	print('xatolik bor')

	ism = input('Ismingizni kiriting:')
	fam = input('Familiyangizni kiriting:')

	if ism or fam:
		print('Tashakur')
	else:
		print('Isim yoki Familiyangizni kiriting')