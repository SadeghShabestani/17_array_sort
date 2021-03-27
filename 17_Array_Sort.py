import termcolor2
list = []
number = int(input("Array Number: "))
for i in range(number):
    num = int(input("Enter Number: "))
    list.append(num)

sort = sorted(list)

if list == sort:
    print(termcolor2.colored(f"Great list: {list}", color="green"))
else:
    print(termcolor2.colored(f"Bad list: {list}", color="red"))
    print(termcolor2.colored(f"Great list: {sorted(list)}", color="green"))