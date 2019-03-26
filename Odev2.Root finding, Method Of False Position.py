def f(x):
    return(x**2-4*x+3)


x1 = int(input("baslangic tahmini(x1): "))
x2 = int(input("bitis tahmini(x2) : "))
# Bu yontemde de x1 ile x2nin fonksiyonu kestigi noktalar arasinda bir dogru
# parcasi cizip o dogru parcasinin x eksenini kestigi noktayi bulup,
# aradigimiz kok xr ile x1 yada x2 ikilisinden hangisi arasinda yer aliyorsa
# ona gore araligi kuculturuz.

if (f(x1) * f(x2) == 0):  # yani fonksiyona gonderdigimiz x'lerden herhangi
    # birinin y degeri 0 ise direk koku bulmusuz demektir.
    print("tahminlerinizden biri denklemin kokudur")
elif (f(x1)*f(x2) > 0):
    print("girdiginiz aralikta tek sayida kok yoktur, \
     0 dahil cift sayida koku olabilir")
else:
    print("Kok(ler), belirlediginiz aralikta bir yerde. Hesaplaniyor...")
    temp = x1
    for i in range(1000):
        xr = (f(x1)*x2-f(x2)*x1)/(f(x1)-f(x2))
        if(abs(f(temp)-f(xr)) < 0.01): #gecen kodda temp-xr demistim, y ile yaklasmak vs x ile yaklasmak arasinda hangisi daha etkili bilmiyorum.
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
