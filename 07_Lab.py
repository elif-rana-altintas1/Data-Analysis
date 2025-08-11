
#!bu çalışmada veri bakım ve onarımı yapacağız.

import pandas as pd
import numpy as np

df= pd.read_csv(
    filepath_or_buffer=r"C:\Users\kursa\Desktop\homewok\04_Data_Analysis\auto.csv",
)
# print(df)

#? veri setimizde sütun başlıkları bulunmamaktadır sütun başlıklarını ekleyelim

df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
              "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
              "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
              "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

# print(df)

#! Hatalı yada eksik verileri saptayalım

#* 1. adım: "?" sembolü yerine numpy kütüphanesinin "nan" value yazdırılır.
df.replace(
    to_replace="?",
    value=np.nan,
    inplace=True
)


#* 2. adım: Missing value sayalım
missing_value_df = df.isnull()

for item in missing_value_df.columns.values.tolist():
    print(
        f"Columns Name: {item}\n"
        f"=================\n"
        f"{missing_value_df[item].value_counts()}\n"
        f"\n"
    )

#print(df.info()) eksik gözlem sayısını vermez ama var mı yok mu onu gösterir.

#* 3. adım : handle missing values

#todo 2 yol var 1. ortalama değeri vermek 2. frekans aralığını vermek
#? ortalama değer vermek
df["normalized-losses"] = (
    df["normalized-losses"].replace(
        to_replace = np.nan,
        value=df["normalized-losses"].astype(float).mean()

        )
    
)

#? frekans aralığını vermek

df["nnum-of-doors"] = (
    df["num-of-doors"].replace(
        to_replace = np.nan,
        value=df["num-of-doors"].value_counts().idxmax()

        )
    
)


#! veri standardizasyonu

df["city_km/l"]=235/ df["city-mpg"]
df["highway_km/l"] = 235 / df["highway-mpg"]

#!NORMALİZASYON & ÖLÇEKLENDİRME

df["length"] = df["length"] / df ["length"] . max ()
df["width"]=df["width"] / df [ "width"].max ()
df["height"] = df["height"] / df ["height"].max()

#!DATA ENCODİNG
dummay_veriable = pd. get_dummies(df["fuel-type"],dtype=float)
#! FEATURES ENGİNEERİNG
#yeni özellikler craft edilir


#! Bakımını yaptığımız veri setini fresh bir excel yazalım
df.to_csv("clean_auto.csv")
