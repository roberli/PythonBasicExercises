number = int(input("Type a number: "))
s_calc = number % 2
s_four = number % 4

if (s_calc != 0):
    print("The number {0} typed is ODD !!!".format(number))
else:
    print("The number {0} typed EVEN !!!".format(number))

if (s_four == 0):
    print("The number {0} is multiple of FOUR and it is EVEN".format(number))
else:
    print("The number {0} is NOT multiple of FOUR".format(number))