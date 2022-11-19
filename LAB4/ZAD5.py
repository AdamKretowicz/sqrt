import random

punkty = [round(random.uniform(0, 50), 2) for i in range(15)]

print(punkty)
print(f'Najwiecej zdobytych punktow: {max(punkty)}, najmniej zdobytych punktow {min(punkty)}')

liczba = float(input("Podaj liczbe punktow: "))

if liczba in punkty:
    print(punkty.index(liczba))
else:
    print("Liczba nie wystepuje")

sumapkt = sum(punkty)
srednia = round(sumapkt/len(punkty), 2)

print("Srednia punktow", srednia)
powyzej = []
for p in punkty:
    if p > srednia:
        powyzej.append(p)
print(powyzej, len(powyzej))
ponizej = [p for p in punkty if p < srednia]
print(ponizej, len(ponizej))



