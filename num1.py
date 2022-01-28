import pandas as pd
import numpy as np

#1. Numpy’da Vektor ve Matrisin farkini tek cumle ile ifade ediniz.
#Vektor is an array with a single dimension. but matris refers to two or more dimensions.

#2. 10 elemanli bir listeden NumPy Array’i olusturunuz.
b=np.array([1,2,3,4,5,6,7,8,9,10])
print(b)
#[ 1  2  3  4  5  6  7  8  9 10]

#3. Icerisinde ‘0’ lar olan, ve veri tipi integer olan 10X10’luk bir matris olusturunuz.
a=np.zeros((10,10),dtype=int)
print(a)
# [[0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]]

#4. Icerisinde ‘1’ ler olan, veri tipi float olan 10X10’luk bir matris olusturunuz.
c=np.ones((10,10), dtype=float)
print(c)
# [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

#5.	Icerisinde ‘9’ lar olan, veri tipi integer olan 10X10’luk bir matris olusturunuz.
d=np.full((10,10),9,dtype=int)
print(d)
# [[9 9 9 9 9 9 9 9 9 9]
#  [9 9 9 9 9 9 9 9 9 9]
#  [9 9 9 9 9 9 9 9 9 9]
#  [9 9 9 9 9 9 9 9 9 9]
#  [9 9 9 9 9 9 9 9 9 9]
#  [9 9 9 9 9 9 9 9 9 9]
#  [9 9 9 9 9 9 9 9 9 9]
#  [9 9 9 9 9 9 9 9 9 9]
#  [9 9 9 9 9 9 9 9 9 9]
#  [9 9 9 9 9 9 9 9 9 9]]

#6.	5 ile 25 arasinda, 3’er 3’er atlayan tek boyutlu bir Array olusturunuz.
e=np.arange(5,25,3)
print(e)
# [ 5  8 11 14 17 20 23]

#7. -1 ile 1 arasinda 30 adet Array olusturunuz.
f=np.linspace(-1,1,30)
print(f)
# [-1.         -0.93103448 -0.86206897 -0.79310345 -0.72413793 -0.65517241
#  -0.5862069  -0.51724138 -0.44827586 -0.37931034 -0.31034483 -0.24137931
#  -0.17241379 -0.10344828 -0.03448276  0.03448276  0.10344828  0.17241379
#   0.24137931  0.31034483  0.37931034  0.44827586  0.51724138  0.5862069
#   0.65517241  0.72413793  0.79310345  0.86206897  0.93103448  1.        ]

#8.	0 ile 30 arasinda 5x6’lik bir matris olusturun.
g=np.random.randint(0,30,(5,6))
print(g)
# [[24 22 20 15 17 15]
#  [15 16  9  2 12 21]
#  [23 28 25  1 29 18]
#  [ 7 19  0 12 23 10]
#  [ 2  7  5 22 16  3]]

# 9.	Kosegenleri 1 olan 10x10’luk bir matris olusturunuz. 

h=np.eye(10)
print(h)
# [[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]

# 10. 0 ile 10 arasinda 5x10’lik bir matris olusturun. (integer) ve bu matrisin;
# * a. eleman sayisini 
# * b. boyut bilgisini/sayisini 
# * c. satir X sutun bilgisini 
# * d. veri tipini numpy metodlariyla yazdiriniz.

i=np.random.randint(0,10,(5,10))
print("eleman sayisi: ",i.size)
print("boyut bilgisi sayisi: ",i.ndim)
print("satir x sutun bilgisi: ",i.shape)
print("veri tipi: ",i.dtype)
# eleman sayisi:  50
# boyut bilgisi sayisi:  2
# satir x sutun bilgisi:  (5, 10)
# veri tipi:  int32

# 11. 0 ile 10 arasindaki degerlerden olusan 3 adet 4x7’lik bir matris olusturunuz. (3 boyutlu bir matris olusturulacak)
j=np.random.randint(10,size=(3,4,7))
print(j)
#  [[5 0 5 2 1 7 8]
#   [2 8 6 7 6 8 3]
#   [9 2 2 4 8 0 6]
#   [4 6 3 5 7 3 4]]]

# 12. Bir vektor olusturunuz ve daha sonrasinda ayni vektoru bir matrise ceviriniz. (boyut sayisini degistirin.)
k=np.arange(1,10).reshape(3,3)
print(k)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

#  13. 4 tane ayri tek boyutlu array’i birlestirerek bir array olusturunuz.
l=np.array([1,2,3])
m=np.array([4,5,6])
n=np.array([7,8,9])
o=np.array([10,11,12])
p=np.concatenate([l,m,n,o])
print(p)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

#14. 2 boyutlu bir vektor ve bir matris olusturun(ayri ayri), bu iki arrayi numpy metodlarini kullanarak sutun bazli birlestiriniz,
r=np.array([[1,2,3],[4,5,6]])
s=np.array([[7,8,9],[10,11,12]])
t=np.concatenate([r,s],axis=1)
print(t)
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]

# 15. Numpy’da “axis=1” ve “axis=0” arasinda ne fark vardir. Teorik olarak yaziniz?
# axis=0 means that rows, shows x axis
# axis=1 means that columns, shows y axis

#16. Farkli boyutlardaki arraylari satir ve sutun bazli ayri ayri birlestiriniz.
u=np.array([[1,2,3,],[10,11,12]])
v=np.array([[4,5,6],[7,8,9]])
y=np.vstack([u,v])
z=np.hstack([u,v])
print(y)
print(z)
# [[ 1  2  3]
#  [10 11 12]
#  [ 4  5  6]
#  [ 7  8  9]]
# [[ 1  2  3  4  5  6]
#  [10 11 12  7  8  9]]

# 17. 10 elemanli bi liste olusturunuz ve bu listeyi Numpy metodlariyla bolerek(split) 4 ayri array olusturunuz.
ab=[1,2,3,4,5,6,7,8,9,10,11,12]
ac=np.split(ab,[2,5,7])
print(ac)
# [array([1, 2]), array([3, 4, 5]), array([6, 7]), array([ 8,  9, 10, 11, 12])]

#  18. Random bir array olusturunuz ve bu arrayi buyukten kucuge dogru siralayiniz. Sonra hangi elemanin hangi indexte oldugunu gosteren bir metod uygulayiniz.
ad=np.random.randint(10,size=10)
ae=np.sort(ad)
print(ae)
def index(x):
    a=0
    while a <=len(x):
        for i in range(len(ae)):
            print(ae[a],"is in the index:",i)
            a+=1
        return print
index(ae)
# [1 1 3 3 3 3 3 4 5 8]
# 1 is in the index: 0
# 1 is in the index: 1
# 3 is in the index: 2
# 3 is in the index: 3
# 3 is in the index: 4
# 3 is in the index: 5
# 3 is in the index: 6
# 4 is in the index: 7
# 5 is in the index: 8
# 8 is in the index: 9

# 19. 20 elemanli random bir vektor olusturunuz. Bu vektorun 3. 5. ve 7. elemanlarina ulasin.
af=np.random.randint(20,size=20)
print(af[3])
print(af[5])
print(af[7])
# 11
# 15
# 12

# 20. 10 elemanli random bir vektor olusturunuz ve bu arrayin 4. elemanini farkli bir sayiyla degistiriniz.
ag=np.random.randint(10,size=10)
ag[3]=24
print(ag)
# [ 1  2  3 24  9  3  6  7  0  7]

#21. “Diagonal Matrix” ve “Trace Matrix” kavramlari hakkinda bir arastirma yapip bunlarin ne oldugunu belirten kucuk bir aciklama yaziniz.


#22. 5x5’lik Diagonal bir matris olusturunuz ve Diagonaline denk gelen indexlere ulasiniz.(ayri ayri)



#23. 10 ile 20 arasinda bir vektor olusturunuz. Ve 3. indexten son indexe kadar olan degerleri yazdiriniz.
aj=np.arange(10,20)
print(aj[3:])
# [13 14 15 16 17 18 19]

#24. 10X10 luk bir matris olusturunuz ve 3.satirin 5.sutununa ulasiniz. Ayrica;
# * a. 5.sutunun tum satirlarina ulasiniz. 
# * b. Tum sutunlarin 2.satirlarina ulasiniz. 
# * c. tum sutunlarin 2 ile 7 arasindaki satirlarina ulasiniz. 
# * d. satir indexi 2’den 5’e ve sutun indexi 3 den 7’ye kadar olan degerlere ulasiniz. 
# * e. satir indexi 5’den en sona ve sutun indexi en bastan 4’e kadar olan degerlere ulasiniz. 
# * f. sutun indexi sadece 3, 6,9 olan kolonlarin(sutunlarin), tum satirlarina ulasiniz. 
# * g. 5. indexli satir ve 5.indexli sutuna denk gelen degeri, dogum yilinizla degistiriniz.

ak=np.random.randint(10,size=(10,10))
print(ak)
# [[1 5 5 6 3 7 9 6 0 1]
#  [3 3 1 7 4 8 8 4 6 5]
#  [0 0 5 7 5 4 5 7 8 6]
#  [7 3 0 8 9 3 6 6 7 2]
#  [1 3 5 0 9 3 0 0 0 9]
#  [1 7 6 6 0 9 4 1 8 5]
#  [4 6 0 6 2 9 3 5 3 6]
#  [8 3 1 8 7 9 7 2 1 2]
#  [5 5 3 6 9 0 9 9 9 8]
#  [9 4 0 2 2 3 3 5 5 8]]
print(ak[3,5])
# 3
print(ak[:,5])
# [7 8 4 3 3 9 9 9 0 3]
print(ak[2,:])
# [0 0 5 7 5 4 5 7 8 6]
print(ak[2:7,:])
# [[0 0 5 7 5 4 5 7 8 6]
#  [7 3 0 8 9 3 6 6 7 2]
#  [1 3 5 0 9 3 0 0 0 9]
#  [1 7 6 6 0 9 4 1 8 5]
#  [4 6 0 6 2 9 3 5 3 6]]
print(ak[2:5,3:7])
# [[7 5 4 5]
#  [8 9 3 6]
#  [0 9 3 0]]
print(ak[5:,:4])
# [[1 7 6 6]
#  [4 6 0 6]
#  [8 3 1 8]
#  [5 5 3 6]
#  [9 4 0 2]]
print(ak[:,[3,6,9]])
# [[6 9 1]
#  [7 8 5]
#  [7 5 6]
#  [8 6 2]
#  [0 0 9]
#  [6 4 5]
#  [6 3 6]
#  [8 7 2]
#  [6 9 8]]
#  [2 3 8]]\
ak[5,5]=1983
print(ak)
# [   1    5    5    6    3    7    9    6    0    1]
#  [   3    3    1    7    4    8    8    4    6    5]
#  [   0    0    5    7    5    4    5    7    8    6]
#  [   7    3    0    8    9    3    6    6    7    2]
#  [   1    3    5    0    9    3    0    0    0    9]
#  [   1    7    6    6    0 1983    4    1    8    5]
#  [   4    6    0    6    2    9    3    5    3    6]
#  [   8    3    1    8    7    9    7    2    1    2]
#  [   5    5    3    6    9    0    9    9    9    8]
#  [   9    4    0    2    2    3    3    5    5    8]]


#  25. 0’dan 50’ye kadar 5’er 5’er atlayarak giden bir array olusturunuz (tek boyutlu) ve numpy metodlariyla asagidaki islemleri uygulayin;
al=np.arange(0,50,5)
print(al)
# [ 0  5 10 15 20 25 30 35 40 45]

# * a. 20 den buyuk olan kac deger var.
an=np.sum(al>20)
print(an)
# 5
# * b. 30’dan kucuk kac deger var 
am=np.sum(al<30)
print(am)
# 6

# * c. icerisinde 33 gecen kac deger var 
ao=np.sum(al==33)
print(ao)
# 0

# * d. olusturulan arrayin tum elemanlarini 5 ile carpin.
ap=al*5
print(ap) 
# * e. olusturulan arrayin tum elemanlarinin 2 ile bolumunden kalanlari yazdiriniz.
ar=al%2
print(ar)
# [0 1 0 1 0 1 0 1 0 1]


# 26. 0 ile 1 arasinda 50 elamanli bir array olusturunuz ve ortalamasini aliniz. Ayrica;
at=np.random.rand(1,50)
print(at.mean())
# * a. standart sapmasini aliniz.
print(at.std()) 
# * b. varyansini aliniz.
print(at.var()) 
# * c. median’ini aliniz. 
print(np.median(at))
# * d. en kucuk degeri bulunuz. 
print(np.min(at))
# * e. en buyuk degeri bulunuz.
print(np.max(at))

# 0.4487710995751097
# 0.2854078879509834
# 0.08145766250464108
# 0.411027046119961
# 0.03043971324185779
# 0.9573267799405423

# 27.	Pandas seriler ve numpy arrayler arasindaki farklar nelerdir yaziniz.
#Panda can have different data types and it can be changed in the index

# 28.	Indexi buyuk harflerden olusan, icinde farkli veri tipleri bulunan 5 elemanli bir seri olusturunuz.
seri=pd.Series([1,1.5,False,True,None],index=('A','B','C','D','E'))
print(seri)
# A        1
# B      1.5
# C    False
# D     True
# E     None

#29.	Key’ler ulke adlari, value’lar baskentleri olacak sekilde 5 elemanli bir sozluk olusturup onu seriye ceviriniz. (ornek: fransa:paris)
dict={'Turkey':'Ankara','Netherlands':'Amsterdam','Abd':'Washington','England':'London','Spain':'MAdrid'}
seri1=pd.Series(dict)
print(seri1)
# Turkey             Ankara
# Netherlands     Amsterdam
# Abd            Washington
# England            London
# Spain              MAdrid

# 30.	10 elemanli random bir vektor olusturun.
# * Vektoru seriye cevirip indexleri str olarak belirleyin. 
# (ornek: a,b,c,d,e,f,g.. seklinde)
# * Index ismine gore serinin 3. elemanina ulasin. 
# (ornek: c indexine karsilik gelen deger)
# * Serinin index sirasina gore 1. Elamanina ulasin.
# * Index ismine gore serinin  2. Ve 7. Elemanlarina ayni anda ulasin. 
# (Ornek: b ve g indexine karsilik gelen degerler)
# * Index ismi ile serinin 2. Ve 7. Elemanlari arasindaki degerleri yazdirin.
# (Ornek: b,c,d,e,f,g indexlerine karsilik gelen degerler)
# * Index sirasiyla serinin 4. indexinden son indexine kadar olan degerleri yazdirin.

ax=np.random.randint(10,size=10)
seri2=pd.Series(ax,index=('A','B','C','D','E','F','G','H','I','J'))
print(seri2)
print(seri2['C'])
print(seri2[0])
print(seri2[['B','G']])
print(seri2['B':'G'])
print(seri2[3:])
# A    5
# B    7
# C    9
# D    2
# E    9
# F    8
# G    6
# H    2
# I    7
# J    7
# dtype: int32
# 9
# 5
# B    7
# G    6
# dtype: int32
# B    7
# C    9
# D    2
# E    9
# F    8
# G    6
# dtype: int32
# D    2
# E    9
# F    8
# G    6
# H    2
# I    7
# J    7
# dtype: int32