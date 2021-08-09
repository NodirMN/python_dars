#ikki xil vaqt kiritiladi
# time1 = soat1, minut1, secund1
# time2 = soat2, minut2, secund2

soat1 = int(input('1-soat:'))
minute1 = int(input('1-minut:'))
secund1 = int(input('1-secund:'))


soat2 = int(input('2-soat:'))
minute2 = int(input('2-minut:'))
secund2 = int(input('2-secund:'))


# 1 soat 3600 secund
secund = (soat2-soat1)  * 3600 + (minute2-minute1) * 60 + (secund2-secund1)
print('secund:{}'.format(secund))