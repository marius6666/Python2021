import random
n = [random.randint (-999, 999) for i in range (10)]
Spisok = len(n)
print("Список", str(n))

nechetnye = []
for i in range(Spisok):
    if n[i] % 2 != 0:
        nechetnye.append(n[i])

def maksimalnoe ():
    maximum= nechetnye[0]
    for i in range(1, len(nechetnye)):
            if nechetnye[i] > maximum:
                maximum = nechetnye[i]
    print ('Наибольший нечетный элемент:', maximum)

maksimalnoe()

def minimummodul ():
    minimum = abs(n[0])
    for i in range(Spisok):
        if abs(n[i]) < minimum:
            minimum = abs(n[i])
    print('Минимальный элемент списка по модулю:', minimum)

minimummodul ()

maksimalnoe()     #проверяю, как вызываются функции еще разок :)
minimummodul ()