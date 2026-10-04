a=input()
count=0
for i in (a):
    is_vowel=i=="a" or i=="e" or i=="i" or i=="o" or i=="u"
    if is_vowel:
        count=count+1
if count>2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")
