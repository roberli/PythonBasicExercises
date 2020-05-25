number = int(input("Please type a number: "))

o_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n_list = []

for x in o_list:
    if x < number:
        n_list.append(x)
print("The number {0} is the limit of List".format(number), n_list)