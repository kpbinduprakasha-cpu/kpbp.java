a = int(input())
for i in range(3):
    print("outer:" + str(i))
    for j in range(7, 9):
        print("inner:" + str(j))
print("end")
