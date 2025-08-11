
import pandas as pd
import numpy as np
dict = {
    "a":10,
    "b":20,
    "c":30
}

#?pandas kütüphanesinde 2 ana veri tutma şekli vardır. Bunlardan birincisi series diğeri ise Dataframe'dir.
pd_series = pd.Series(dict)
print(pd_series)

#pandas series ve Dataframe uygulama built in fonksiyonlar
print (pd_series.shape) #serinin yada dataframe kaç satır ve sütundan oluştuğunu söyler

print(pd_series.dtype)  #tipleri döner

print(pd_series.ndim)   #serinin kaç katmanlı olduğunu söyler

print(pd_series.describe())    #veri seti ile ilgili count , mean, std , miv ve max değerlerini verir.

print(pd_series.head())     #veri setinin ilk 5 satırını döner lakin argüman olan verilen satır sayısında döner


print(pd_series.tail())       #head fonksiyonun tam tersi mantıkla çalışır

#*şartın tutup tutmama durumuna göre true false dönen şart yapıları

print(pd_series > 10)

print(pd_series % 2 == 0)


#? Dataframe

df = pd.DataFrame(
    data=np.random.rand(3,5),
    index=["A","B","C"],
    columns=["Column1","Column2","Column3","Column4","Column5"]

)

print(df)

#! SELECT işlemleri

print(df["Column1"]) #? sadece column1 sütununu seçer ve tipi series olur

print(df[["Column1","Column2"]]) #?birden fazla sütun seçilfiğinde tip Dataframe olur


#!birden fazla sütunu aşağıdaki gibi dışarı çıkartamayız
#todo print(df["Column1","Column2"])

#!loc[] --> loc yapısı ile satır ve sütunları seçebiliriz 
#? loc yapısının ile alacağı değer index ikinci alacağı değer column değeridir
#todo loc yapısı label yani etiket bazlı seçim yapar

print(df.loc["A"]) #?A satırını seçer ve tip seriese olur
print(df.loc[["A","C"]])  #?A VE C satırlarını seçer tipi dataframe olur
print(df.loc["A", "Column3"])  #? Tek bir hücre getirir, tipi: scalar (örneğin: int, float, str)


print(df.loc[["A", "C"], ["Column1", "Column2"]])  # ?DataFrame döner

print(df.loc[:,["Column1","Column2"]]) #Tüm satırlardaki column1 ve column2 sütünlarını seçer ve tipi dataframe olur