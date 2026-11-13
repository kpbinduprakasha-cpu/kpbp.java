country = input()
resultant_string = ""

for i in range(2, len(country)):
    for j in range(0,1):
        resultant_string = resultant_string + country[i]
print(resultant_string)
