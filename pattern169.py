a = input()
a_lower = a.lower()
if a_lower == a_lower[::-1]:
    print("True")
else:
    print("False")
