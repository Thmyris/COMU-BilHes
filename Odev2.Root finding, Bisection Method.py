# Degistirilebilir bir kod olmasi icin f(x) i ayri yazacagiz.
def f(x):
    return(x**2-4*x+3)


# kokleri 1 ve 3, y'yi 3'te kesiyor.
# Bu yontemde 2 tahmin alip cebir kullanarak o tahminimizin
x1 = int(input("baslangic tahmini(x1) : "))
x2 = int(input("bitis tahmini(x2) : "))


if (f(x1) * f(x2) == 0):  # yani fonksiyona gonderdigimiz x'lerden herhangi
    # birinin y degeri 0 ise direk koku bulmusuz demektir.
    print("tahminlerinizden biri denklemin kokudur")
elif (f(x1)*f(x2) > 0):
    print("girdiginiz aralikta tek sayida kok yoktur, 0 dahil cift sayida koku olabilir")
else:
    print("Kok(ler), belirlediginiz aralikta bir yerde. Hesaplaniyor...")
    temp = x1
    for i in range(1000):
        xr = (x1+x2)/2
        if(abs(temp-xr) < 0.01):
            print("kok bulundu: ", xr)
            print("Hesaplama bitene kadar 2ye bolme miktari: ", i+1)
            break
        if(f(xr) == 0):
            print("kok bulundu: ", xr)
            print("Hesaplama bitene kadar 2ye bolme miktari: ", i+1)
            break
        elif(f(xr)*f(x1) < 0):  # kok x1 ile xr arasinda
            x2 = xr
        else:  # kok xr ile x2 arasinda
            x1 = xr
        temp = xr
        print(xr)
