Summa = 0
SkokaBiletaff = input("Введите желаемое количество билетов :")
Summa, SkokaBiletaff = int(Summa), int(SkokaBiletaff)
for i in range(SkokaBiletaff):
    Vozrast = int(input("Введите возраст :"))
    StoimBileta = 0
    if Vozrast < 18:
        StoimBileta = 0
    elif 18 <= Vozrast < 25:
        StoimBileta = 990
    elif Vozrast >= 25:
        StoimBileta = 1390
    Summa = Summa + StoimBileta
if SkokaBiletaff > 3:
    Summa = Summa * 0.9
    print('Вы купили больше 3-х билетов и вам положена скидка в 10% от суммы заказа')
print('Стоимость билетов равна —', Summa)
