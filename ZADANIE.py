while True:
    Posled = input("Введите несколько целых чисел через пробел,если введете не целые числа или не цифры,то программа вернется к началу ")
    Randomzifra = int(input("Введите любое случайное число в диапазоне чисел введенных ранее, если введете слишком большое число, то программа вернется к началу "))
    Spisok = Posled.split()
    Spisok2 = ''.join(Spisok)
    if Spisok2.isdigit() ==False:
        continue
    elif Randomzifra > max(list(map(int, Spisok))):
        continue
    else:
        break
print("Введенная последовательность,преобразованная в список ", Spisok)
SpisokIsZifr = list(map(int, Spisok))



for i in range(len(SpisokIsZifr)):
    for j in range(len(SpisokIsZifr) - i - 1):
        if SpisokIsZifr[j] > SpisokIsZifr[j + 1]:
            SpisokIsZifr[j], SpisokIsZifr[j + 1] = SpisokIsZifr[j + 1], SpisokIsZifr[j]


print("Отсортированный список ", SpisokIsZifr)

Spisok3 = []
Spisok3.append(Randomzifra)

Spisok4 = Spisok3 + Spisok

SpisokIsZifr2 = list(map(int, Spisok4))



for i in range(len(SpisokIsZifr2)):
    for j in range(len(SpisokIsZifr2) - i - 1):
        if SpisokIsZifr2[j] > SpisokIsZifr2[j + 1]:
            SpisokIsZifr2[j], SpisokIsZifr2[j + 1] = SpisokIsZifr2[j + 1], SpisokIsZifr2[j]


Pered1 = SpisokIsZifr2.index(Randomzifra)-1
Posle1 = SpisokIsZifr2.index(Randomzifra)+1

ChisloPered = SpisokIsZifr2[Pered1]
ChisloPosle = SpisokIsZifr2[Posle1]


IndPered = SpisokIsZifr.index(ChisloPered)
IndPosle = SpisokIsZifr.index(ChisloPosle)
if IndPered-IndPosle > 1:
    print("В следующий раз вводите число больше 0")
else:
    print('Индекс числа меньше введенного = ', IndPered)
    print('Индекс числа больше введенного = ', IndPosle)












