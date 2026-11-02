a = input()

upper = any(i.isupper() for i in a)
lower = any(i.islower() for i in a)
digite = any(i.isdigit() for i in a)
if upper and lower and digite:
    print("Valid Password")
else:
    print("Invalid Password")
