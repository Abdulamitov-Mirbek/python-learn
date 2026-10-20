# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     print("sandy tuura kirgiz")



# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("sandy tuura kirgiz")


# try
# except
# ValueError
# ZeroDivisionError
# bir neche except
# else
# finally

# try:
#     a = int(input("first number:  "))
#     b = float(input("second number:  "))
#     print(a / b)
# except ValueError:
#     print("sozsuz turdo san jaz")
# except ZeroDivisionError:
#     print("0go bolunboit!")
# except Exception as e:
#     print(e)


# ValueError - tuura emes maaniny bergende chygat
# ZeroDivisionError - 0go bolungondo je dolundogondo chygat

# try:
#     numbr = int(input("Enter a number: "))
# except ValueError:
#     print("san kirgiz")
# else:
#     print("tuura")
#     print("sen kirgizgen ssan:", numbr)


# else - kata chykpagan uchurda ishteit

# try:
#     number = int(input("Enter a number: "))
#     print(number)
#
# except ValueError:
#     print("tuura emes kata ondo ")
# except ZeroDivisionError:
#     print("0go bolunboit!")
# else:
#     print("tuura")
#     print("sen kirgizgen ssan:", number)
# finally:
#     print("programma ayaktady")

# finally - kata chyksa dagy, chykpasa dagy ishtei beret

# КООПСУЗ БӨЛҮҮ
# Колдонуучудан эки сан ал. Биринчи санды экинчи санга бөл.
# Талаптар:
# туура эмес сан киргизилсе ValueError карма;
# 0гө бөлүүгө аракет кылынса ZeroDivisionError карма;
# ката болбосо else аркылуу жыйынтыкты чыгар;
# finally аркылуу "Программа аяктады" деп чыгар.
# ЖАШ ТЕКШЕРҮҮ
# Колдонуучудан жашын input() аркылуу ал.
# Эгер колдонуучу сан эмес нерсе киргизсе: "Жашты сан менен киргизиңиз" деп чыгар.
# Эгер туура сан киргизилсе:
# 18 же андан чоң болсо "Кирүүгө уруксат"
# 18ден кичине болсо "Кирүүгө уруксат жок"
# else колдон.
# КАЛЬКУЛЯТОР
# Колдонуучудан:
# биринчи сан
# экинчи сан
# операция (+, -, *, /)
# ал.
# Мисалы: 10 5 +
# Натыйжа: 15
# Талаптар:
# туура эмес сан үчүн ValueError;
# 0гө бөлүү үчүн ZeroDivisionError;
# белгисиз операция киргизилсе өзүнчө билдирүү чыгар;
# finally колдон.
# САНДЫН КВАДРАТЫ
# Колдонуучудан сан ал.
# Эгер туура сан киргизилсе, анын квадратын чыгар.
# Эгер туура эмес маалымат киргизилсе: "Сан гана киргизиңиз" деп чыгар.
# else жана finally колдон.
# LIST МЕНЕН ИШТӨӨ
# Берилген:
# numbers = [10, 20, 30, 40, 50]
# Колдонуучудан индекс ал.
# Ошол индекстеги элементти чыгар.
# Мисалы: Индекс: 2 Натыйжа: 30
# Эгер индекс туура эмес болсо, катаны карма.
# Ката үчүн билдирүү чыгар жана finally колдон.
# БАНКТЫК ЭСЕП
# Баштапкы баланс:
# balance = 10000
# Колдонуучудан алынуучу акчанын суммасын сура.
# Талаптар:
# сумма сан болушу керек;
# сумма 0дөн чоң болушу керек;
# сумма баланстан көп болсо акча берүүгө болбойт;
# туура болсо балансты азайт;
# else аркылуу операция ийгиликтүү болгонун чыгар;
# finally аркылуу "Операция аяктады" деп чыгар.
# БАҢА КИРГИЗҮҮ
# Колдонуучудан студенттин баасын ал.
# Баасы 1ден 5ке чейинки сан болушу керек.
# Эгер: 5 → "Абдан жакшы" 4 → "Жакшы" 3 → "Канааттандырарлык" 2 же 1 → "Начар"
# Эгер сан эмес маалымат киргизилсе ValueError карма.
# Эгер 1–5 диапазонунан тышкары сан киргизилсе өзүнчө билдирүү чыгар.
# БИР НЕЧЕ САНДЫН БӨЛҮНДҮСҮ
# Колдонуучу 5 сан киргизиши керек.
# Ар бир санды 100гө бөлүп чыгар.
# Эгер колдонуучу сан эмес маалымат киргизсе ValueError карма.
# Эгер 0 киргизилсе ZeroDivisionError чыгышы мүмкүн болгон операция түз.
# Ар бир операцияда программа токтоп калбагандай кылып иштет.
# 🔥 КИРҮҮ СИСТЕМАСЫ
# Туура username жана password алдын ала берилсин:
# username = "admin" password = "12345"
# Колдонуучудан username жана password сура.
# Талаптар:
# программа ката менен токтоп калбашы керек;
# password бош болсо билдирүү чыгар;
# username туура болсо жана password туура болсо "Кош келиңиз!" деп чыгар;
# туура эмес болсо "Маалымат туура эмес" деп чыгар;
# finally колдон.
# 🔥 КАЛЬКУЛЯТОР 2.0
# Толук калькулятор түз.
# Колдонуучу:
# Биринчи сан
# Экинчи сан
# Операция
# киргизет.
# Колдоого алынган операциялар: +
# /
# Мисалы:
# Биринчи сан: 20 Экинчи сан: 5 Операция: /
# Натыйжа: 4
# Талаптар:
# ValueError карма;
# ZeroDivisionError карма;
# туура эмес операцияны текшер;
# try / except / else / finally колдон;
# программа ката болсо да токтоп калбагандай кыл.