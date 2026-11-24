a=int(input())
year=int(a/365)
rem_day=a-(year)*365
week=int(rem_day/7)
days=rem_day-(week)*7
print(year)
print(week)
print(days)
