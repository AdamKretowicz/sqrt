import random
n = int(input("podaj liczbe elementow "))
zestaw1 = []
for i in range(0, n-1):
    k = random.randint(1, 10)
    zestaw1.append(k)
print(zestaw1)

n = int(input("podaj liczbe elementow "))
zestaw2 = [random.randint(5, 15) for i in range(n)]
print(zestaw2)
x = int(input("Podaj liczbe"))
if x in zestaw1:
    print('Liczba z zestawu1', x)
elif x in zestaw2:
    print('Liczba z zestawu2', x)
# elif x in (zestaw1 or zestaw2):
#     print('Liczba znajduje się w obu zestawach', x)
else:
    print('Nie ma takiej liczby w obu zestawach')

zestaw12 = zestaw1 + zestaw2
print(zestaw12)
zestaw12.sort()
print(zestaw12)

