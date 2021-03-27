import termcolor2

# list = [input("Enter List: ")]
list = list(input("Enter List: "))

if list == sorted(list):
    print(termcolor2.colored(f"Great list: {list}", color="green"))
else:
    print(termcolor2.colored(f"Bad list: {list}", color="red"))
    print(termcolor2.colored(f"Great list: {sorted(list)}", color="green"))
