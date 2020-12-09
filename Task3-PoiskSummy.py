# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

#n = int(input("Введите число: "))
#sum = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
#print("Итого: %.0f" % sum)

n=str(int(input("Введите число: ")))
b=int(n)+int(n+n)+int(n+n+n)
print("Итого: %d" % b)