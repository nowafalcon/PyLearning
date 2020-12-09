#name = input("Say your Name  ")
#surname = input("Привет, " + name + ", а фамилия?  ")
#age = int(input('А годиков тебе сколько ,' + name + ' ' + surname + '? '))
#print("Уважаемый " + name + " " + surname + ", в вашем возрасте, а если Вам верить, то "
#      + str(age) + ", пора бы перестать играть с такими вещами =)")

name = input("Say your Name  ")
surname = input("Привет, %s, а фамилия?  " % name)
age = int(input("А годиков тебе сколько, %s %s ? " % (name, surname)))
print("Уважаемый %s %s, в вашем возрасте, а если Вам верить, то %f ,"
      "пора бы перестать играть с такими вещами =)" % (name, surname, age))
