a = int(input())

number_1000 = a // 1000
print("1000:" + str(number_1000))

number_500 = a - (number_1000 * 1000)
value_500 = number_500 // 500
print("500:" + str(value_500))

number_100 = number_500 - (value_500 * 500)
value_100 = number_100 // 100
print("100:" + str(value_100))

number_50 = number_100 - (value_100 * 100)
value_50 = number_50 // 50
print("50:" + str(value_50))

number_20 = number_50 - (value_50 * 50)
value_20 = number_20 // 20
print("20:" + str(value_20))

number_5 = number_20 - (value_20 * 20)
value_5 = number_5 // 5
print("5:" + str(value_5))

number_1 = number_5 - (value_5 * 5)
value_1 = number_1 // 1
print("1:" + str(value_1))
