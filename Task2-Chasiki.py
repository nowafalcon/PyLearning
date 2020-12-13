# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте
# форматирование строк.

initial=int(input("Print number of seconds: "))
days=initial//86400
hrs=initial%86400//3600
mins=initial%3600//60
secs=initial%60
if days!=0:
    print(f"Days:{days} and {hrs:02}:{mins:02}:{secs:02}")
else:
    print(f"{hrs:02}:{mins:02}:{secs:02}")