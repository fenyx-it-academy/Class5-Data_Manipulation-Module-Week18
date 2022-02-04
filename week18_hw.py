import numpy as np


# DATA MANIPULATION WEEK-18 ASSIGNMENT

### 1. Numpy’da Vektor ve Matrisin farkini tek cumle ile ifade ediniz.

#Vektör, tek boyutlu bir dizidir (satır ve sütun vektörleri arasında fark yoktur), matris ise iki boyutlu bir diziyi ifade eder"

### 2. 10 elemanli bir listeden NumPy Array’i olusturunuz.

a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99, 100])

### 3. Icerisinde ‘0’ lar olan, ve veri tipi integer olan 10X10’luk bir matris olusturunuz.

b=np.zeros((10,10),dtype='int')

### 4. Icerisinde ‘1’ ler olan, veri tipi float olan 10X10’luk bir matris olusturunuz.

c=np.ones((10,10), dtype = 'float32')
### 5.	Icerisinde ‘9’ lar olan, veri tipi integer olan 10X10’luk bir matris olusturunuz.

d=np.full((10,10),9, dtype='int')  

### 6.	5 ile 25 arasinda, 3’er 3’er atlayan tek boyutlu bir Array olusturunuz.

e=np.arange(5,25,3) 

### 7. -1 ile 1 arasinda 30 adet Array olusturunuz.

f=np.linspace(-1,1,30) 

### 8.	0 ile 30 arasinda 5x6’lik bir matris olusturun.

g=np.random.randint(0,30, (5,6)) 

### 9.	Kosegenleri 1 olan 10x10’luk bir matris olusturunuz. 

gg=np.eye(10) 


### 10. 0 ile 10 arasinda 5x10’lik bir matris olusturun. (integer) ve bu matrisin;

i=np.random.randint(10, size =(5,10)) 

#a. eleman sayisini 
#b. boyut bilgisini/sayisini 
#c. satir X sutun bilgisini 
#d. veri tipini numpy metodlariyla yazdiriniz.

print("Boyut sayisi =  ",i.ndim) 
print("satir, sutun bilgisi =  ",i.shape)
print("Toplam eleman sayisi =  ",i.size)
print("Veri tipi =  ",i.dtype)



### 11. 0 ile 10 arasindaki degerlerden olusan 3 adet 4x7’lik bir matris olusturunuz. (3 boyutlu bir matris olusturulacak)

k = np.random.randint(10, size = (3,4,7))

### 12. Bir vektor olusturunuz ve daha sonrasinda ayni vektoru bir matrise ceviriniz. (boyut sayisini degistirin.)

l=np.arange(1,30) 

ll=np.arange(1,30).reshape(2,2)


### 13. 4 tane ayri tek boyutlu array’i birlestirerek bir array olusturunuz.

x=np.array([1,2,3,4])
y=np.array([1,2,3,4])
z=np.array([1,2,3,4])
t=np.array([1,2,3,4])

xx=np.concatenate([x,y,z,t])

### 14. 2 boyutlu bir vektor ve bir matris olusturun(ayri ayri), bu iki arrayi numpy metodlarini kullanarak sutun bazli birlestiriniz,

m = np.array([[9, 8, 7], [6, 5, 4]])

mm=np.random.randint(0,10, (2,2))

mmm=np.hstack([m,mm])


### 15. Numpy’da “axis=1” ve “axis=0” arasinda ne fark vardir. Teorik olarak yaziniz?

#Eksen 0, birinci boyut (satır) ve eksen 1, ikinci boyut (sütun). "

### 16. Farkli boyutlardaki arraylari satir ve sutun bazli ayri ayri birlestiriniz.

o= np.array([1, 2, 3])

oo= np.array([[9, 8, 7], 
                [6, 5, 4]])

ooo=np.vstack([o,oo]) 

print(ooo)

### 17. 10 elemanli bi liste olusturunuz ve bu listeyi Numpy metodlariyla bolerek(split) 4 ayri array olusturunuz.

s=np.array=([1,2,3,4,5,6,7,8,9,10]) 

ss,sss,sss,sssss =np.split(s, [3,6,9])  


### 18. Random bir array olusturunuz ve bu arrayi buyukten kucuge dogru siralayiniz. Sonra hangi elemanin hangi indexte oldugunu gosteren bir metod uygulayiniz.

tt=np.random.randint(20,size=10)

ttt=np.sort(tt) 

print(ttt)



### 19. 20 elemanli random bir vektor olusturunuz. Bu vektorun 3. 5. ve 7. elemanlarina ulasin.

v=np.random.randint(10, size=20)
print(v[3], v[5], v[7])

### 20. 10 elemanli random bir vektor olusturunuz ve bu arrayin 4. elemanini farkli bir sayiyla degistiriniz.

v=np.random.randint(20, size=10)
v[4]=20000
print(v)

### 21. “Diagonal Matrix” ve “Trace Matrix” kavramlari hakkinda bir arastirma yapip bunlarin ne oldugunu belirten kucuk bir aciklama yaziniz.

#Diagonal Matrix=The unit matrix is every nxn square matrix made up of all zeros except for the elements of the main diagonal that are all ones.
#Trace Matrix = It is the sum of the elements on the main diagonal, from the upper left to the lower right, of the matrix.

### 22. 5x5’lik Diagonal bir matris olusturunuz ve Diagonaline denk gelen indexlere ulasiniz.(ayri ayri)

yy=np.eye(5)

print([0,0],x[1,1],x[2,2],x[3,3],x[4,4],[5,5])


### 24. 10X10 luk bir matris olusturunuz ve 3.satirin 5.sutununa ulasiniz. Ayrica;

zz= np.random.randint(10, size = (10, 10))
zz[3:4,4:5]

print(zz)

#a. 5.sutunun tum satirlarina ulasiniz. 
a[:,5]    

#b. Tum sutunlarin 2.satirlarina ulasiniz.
a[2,:] 

#c. tum sutunlarin 2 ile 7 arasindaki satirlarina ulasiniz. 
a[2:7,:] 

#d. satir indexi 2’den 5’e ve sutun indexi 3 den 7’ye kadar olan degerlere ulasiniz.
a[2:5,3:7]  

#e. satir indexi 5’den en sona ve sutun indexi en bastan 4’e kadar olan degerlere ulasiniz. 
a[5:,:4] 


### 25. 0’dan 50’ye kadar 5’er 5’er atlayarak giden bir array olusturunuz (tek boyutlu) ve numpy metodlariyla asagidaki islemleri uygulayin;

eee=np.arange(0,50,5) 

#a. 20 den buyuk olan kac deger var. 
eeee=np.sum(eee > 20)   
print(eeee)

#b. 30’dan kucuk kac deger var
eeeee=np.sum(eee > 30)   
print(eeeee)

#d. olusturulan arrayin tum elemanlarini 5 ile carpin. 
eee*5


### 26. 0 ile 1 arasinda 50 elamanli bir array olusturunuz ve ortalamasini aliniz. Ayrica;

ggg=np.random.randint(0,30, size=50)

print(ggg)
#a. standart sapmasini aliniz. 
#b. varyansini aliniz. 
#c. median’ini aliniz. 
#d. en kucuk degeri bulunuz. 
#e. en buyuk degeri bulunuz.



### 27.	Pandas seriler ve numpy arrayler arasindaki farklar nelerdir yaziniz.



### 28.	Indexi buyuk harflerden olusan, icinde farkli veri tipleri bulunan 5 elemanli bir seri olusturunuz.



### 29.	Key’ler ulke adlari, value’lar baskentleri olacak sekilde 5 elemanli bir sozluk olusturup onu seriye ceviriniz. (ornek: fransa:paris)



### 30.	10 elemanli random bir vektor olusturun.
#Vektoru seriye cevirip indexleri str olarak belirleyin. 
#(ornek: a,b,c,d,e,f,g.. seklinde)
#* Index ismine gore serinin 3. elemanina ulasin. 
#(ornek: c indexine karsilik gelen deger)
#* Serinin index sirasina gore 1. Elamanina ulasin.
#* Index ismine gore serinin  2. Ve 7. Elemanlarina ayni anda ulasin. 
#(Ornek: b ve g indexine karsilik gelen degerler)
#* Index ismi ile serinin 2. Ve 7. Elemanlari arasindaki degerleri yazdirin.
#(Ornek: b,c,d,e,f,g indexlerine karsilik gelen degerler)
#* Index sirasiyla serinin 4. indexinden son indexine kadar olan degerleri yazdirin.



### 31.	2 adet 5 elemanli seri olusturun.
#* Olusturdugunuz serileri birlestirin.
#* Birlesen 10 elemanli serinin indexini 1’den 10’a kadar olacak sekilde duzenleyin.
#* Indexini duzenlediginiz seride, loc ve iloc metodlari ile, indexi 4,5,6 olan degerlere ulasin.



### Master odev ;
#Bir dongu icerisinde random olacak sekilde iki tane 20x20’luk matris uretin ve bu matrislerin farklarini alin. Ve fark matrisinin diagonali, -0.1 ile 0.1 arasinda olana kadar bu islemi tekrarlayin. Istenilen matris bulundugunda program dursun ve toplam kac dongunun kuruldugunu, ne kadar sure icinde buldugunu ve istenilen matrisi print ile birlikte ekrana yazdiriniz. 
#* Tavsiye: 20 x 20 luk matrisin bulunmasi saatler surebilir. Bu yuzden algoritmanizin dogrulugunu test etmek icin once 4x4, 5x5 gibi kucuk matrislerde deneyebilirsiniz. Ve matris sayisisini arttirarak en son 20x20 u deneyebilirsiniz. 
#(Matris uretme islemini np.random.random((a,b)) fonksiyonu ile yapabilirsiniz. 0-1 arasi istenen boyutlarda array uretir.)



