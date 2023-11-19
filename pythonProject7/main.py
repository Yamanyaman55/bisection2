def f(x):
    return x ** 3 + 4 * x ** 2 -10


def bisection_methodu(baslangic_degeri, son_deger):
    a = baslangic_degeri
    b = 4

    if f(a) * f(b) > 0:
        print("Bu aralıkta bir kök yok.")
        return None

    for i in range(son_deger):
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2



baslangic_degeri = float(input("Başlangıç değeri: "))
son_deger = int(input("Maksimum iterasyon sayısı: "))

kok = bisection_methodu(baslangic_degeri, son_deger)

if kok is not None:
    print("Bulunan kök:", kok)

