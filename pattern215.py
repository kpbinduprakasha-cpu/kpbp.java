for i in range(2):
    print("outer:" + str(i))
    for j in range(7, 10):
        print("  inner:" + str(j))
print("end")
