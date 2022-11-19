values = [10, 20, 30]
keys = ['ten', 'twenty', 'thirty']
# d1 = dict(zip(keys, values))
# print(d1)
d1 = {}
for i in range(3):
    d1[keys[i]] = values[i]
print(d1)

d2 = dict(thirty = 30, forty = 40, fifty = 50)
d3 = {}
d3 = d1.copy()
d3.update(d2)
print(d3)

