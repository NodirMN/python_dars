# 1kilogram limon a so'm b tiyin. misol:21 000 so'm 35 tiyin
a = int(input("so'm:"))
b = int(input("tiyin:"))
n = int(input("kg:"))

c = n * ((a * 100) + b)
print("so'm: ", c // 100)
print("tiyin: ", c % 100)