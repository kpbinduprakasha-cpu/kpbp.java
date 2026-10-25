a=int(input())
b=int(input())

end=int(b**0.5)
start=int(a**0.5)
if start*start<a:
    start+=1
count=end-start+1
print(max(0,count))
