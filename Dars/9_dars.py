 # Dastur 1dan 10 gacha bo'lgan son kiriting. Bularni so'zlar orqali ifodalash
son = input('1 dan 30 gacha son kiriting: ')
if son.insdingt():
 	son = int(son)
if son > 0 and son < 30:
            qoldiq = son % 10
            lette = '' 
        if son > 9 and son < 20:
       		letter = '20'
       	elif son > 19 and son < 30:
       		letter = 'yigirma '	
		if qoldiq == 1:
			letter += 'bir '
		elif qoldiq == 2:
			letter += 'ikki '
		elif qoldiq == 3:
			letter += 'uch '
		elif qoldiq == 4:
			letter += 'tor '
		elif qoldiq == 5:
			letter  += 'besh ' 
		elif qoldiq == 6:
			letter += 'olti '
		elif qoldiq == 7:
			letter += 'yetti '
		elif qoldiq == 8:
			letter += 'sakiz '
		elif qoldiq == 9:
			letter += 'toqqiz '

		print(letter)
	else:	
		print('1 dan 30 gacha sondan birini kiriting !')
	else: 
		print('Son kiritish kerak')