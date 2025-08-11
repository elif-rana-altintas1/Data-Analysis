
#!GROUP BY

#*Verilerimizi gruplamak için groupby() fonksiyonunu kullanabiliriz. Verilerimiz belirli bir sütuna ve ilgili sütundaki değerlere göre gruplandırılır. Örneğin,Rating sütununa göre gruplayabiliriz


import pandas as pd 
users = {
    
    'employee name': ['Burak', 'Kerem', 'Elif', 'Munzur', 'Baran'],
    'occupation': ['Kumarbaz', 'Kalpazan', 'Kaçakçı', 'Kalpazan', 'Kumarbaz'],
    'age': [36, 35, 21, 21, 36],
    'income': [5000, 2000, 2000, 2000, 5000],
    'neighbor': ['Sarıyer', 'Suadiye', 'Suadiye', 'Nispetiye','Sarıyer'],
        }
df= pd.DataFrame(users)
print (df)

#! Group by ile birlikte muhakkak bir aggredate fonksiyonu kullanmalıyız.
#*örneğin gruplandırdığımız verileri yaş ortalamasını almak için mean() fonksiyonunu kullanabiliriz
#? mesleklere göre gruplandırdığımız çalılanların maaş toplamlarını bulabiliriz
#todo aggredate fonksiyonlarını :sum(),mean(), count(), min(),max() gibi fonksiyonlar kullanabilir

#!mesleklere göre gelir ortamalası
# result=df.groupby(by= "occupation")["income"].sum()
# print(result)
# #!mesleklere göre yaş ortalamasını allaım 

# result=df.groupby(by="occupation")["age"].mean()
# print(result)

# #!Neighbora göre yaş ortalaması 
# result=df.groupby(by="neighbor")["age"].mean()
# print(result)


