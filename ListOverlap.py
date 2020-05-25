import random
a = []
b = []
c = []

for x in range(1, 11):
    y = random.randint(1, 20)
    a.append(y)

for x in range(1, 11):
    z = random.randint(1, 20)
    b.append(z)

for x in a:
    if x in b:
        c.append(x)
print(sorted(a)) # Only to better understanding of output to fixed de list "c"
print(sorted(b)) # Only to better understanding of output to fixed de list "c"
print(sorted(list(set(c))))