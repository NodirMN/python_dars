
soat1 = int(input("1soat:"))
minut1 = int(input("1minut:"))
secund1 = int(input("1secund:"))

soat2 = int(input("2soat:"))
minut2 = int(input("2minut:"))
secund2= int(input("2secund:"))

secund = (soat2- soat1) * 3600 + (minut2 - minut1) * 60 + (secund2 - secund1)
print("secund: {}".format(secund))