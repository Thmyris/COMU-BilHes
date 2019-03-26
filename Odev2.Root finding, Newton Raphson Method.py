def f(x):
    return(x**2-4*x+3)


def dfdx(x):
    return (2*x-4)


x = int(input("koke yakin bir x sayisi tahmin edin: "))

if (f(x) == 0):  # yani fonksiyona gonderdigimiz x'in
    #  y degeri 0 ise direk koku bulmusuz demektir.
    print("tahmininiz denklemin kokudur")
else:
    print("En yakin kok hesaplaniyor...")
    for i in range(1000):
        tegetde
        if(abs(f(temp)-f(xr)) < 0.01):
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
