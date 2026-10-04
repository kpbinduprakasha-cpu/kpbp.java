a=int(input())
string=str(a)
lenth=len(string)
lenth=int(lenth)
count=0

for i in string:
    sound=int(i)
    sound=sound**lenth
    count=count+sound
print(count)
