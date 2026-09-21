a=int(input())
b=int(input())
c=int(input())

if a==b and a==c and b==c:
    print("Equilateral")
elif a==b or a==c or b==c:
    print("Isosceles")
elif a!=b and a!=c and b!=c:
    print("Scalene")