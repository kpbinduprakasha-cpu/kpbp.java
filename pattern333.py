a=int(input())
for i in range(1,a+1):
    zeros="0 "*(a-i)
    stars="1 "*(2*i-1)
    print(zeros+stars+zeros)