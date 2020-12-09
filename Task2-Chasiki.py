# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте
# форматирование строк.

initial = int(input("Введите число = количество секунд: "))
# days  86400secs
# hrs   3600secs
# mins  60secs
# secs  1secs
days = initial // 86400
hrs = initial % 86400 // 3600
mins = initial % 86400 % 3600 // 60
secs = initial % 86400 % 3600 % 60
if hrs < 10:
    hrs = "0" + str(hrs)
else:
    hrs = str(hrs)
if mins < 10:
    mins = "0" + str(mins)
else:
    mins = str(mins)
if secs < 10:
    secs = "0" + str(secs)
else:
    secs = str(secs)
print("%s : %s : %s" % (hrs, mins, secs))
