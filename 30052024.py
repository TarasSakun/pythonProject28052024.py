user_input = input("Введите 4х значное число: ")
number = int(user_input)
print(number // 1000)
print((number // 100) % 10)
print((number // 10) % 10)
print(number % 10)
