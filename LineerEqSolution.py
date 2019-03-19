#!/usr/bin/python3
# -*- coding: utf-8 -*-

from scipy.linalg import solve

a1, b1, c1 = 1, 2, 1
a2, b2, c2 = 3, 4, -2
# a1x+b1y=c1 ve a2x+b2y=c2 tipindeki iki denklemin çözümünü bulan program
# önce scipy ile bulalım:

print(solve([[a1,b1], [a2,b2]], [c1, c2]))

# şimdi de genişletilmiş katsayılar matrisi üzerinde işlemler yaparak sonucu bulalım

A = [[a1, b1, c1], [a2, b2, c2]]

#A[0] = [-A[1][i]*A[0][1]/A[1][1]+A[0][i] for i in range(3)]
#A[1] = [-A[0][i]*A[1][0]/A[0][0]+A[1][i] for i in range(3)]

# sizden istenen yukarıdaki iki ifadeyi birleştirmenizdir

# print(A[0][2]/A[0][0], A[1][2]/A[1][1])

# print(A[0])

# 2 satirdaki tum 1-0'lari b ile tum 0-1'leri c ile degistirebiliriz.
# Bu indexler birbirlerinin durumlarini kontrol ederek islemlerini gerceklestirirlerse:
c=1
for b in range(0, 2):
    if(b==1):
        c=0
    for i in range(3):
        A[b][i] = -A[c][i]*A[b][c]/A[c][c]+A[b][i]

print(A[0][2]/A[0][0], A[1][2]/A[1][1])
# Bu kodun neden yanlis ciktigini anlayamadim. Yarim saattir ugrasiyorum,
# isin icinden cikamadim. Bu yanlis haliyle githuba gec de olsa yukluyorum.
# Biri yanlisimin sebebini gosterirse minnettar olurum.
