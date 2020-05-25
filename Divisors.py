number = int(input("Please type a number: "))
n_list = []

for x in range(1, number + 1):
    if number % x == 0:
        n_list.append(x)
print(n_list)