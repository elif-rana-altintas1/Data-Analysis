

import pandas as pd

df= pd.read_csv(
    filepath_or_buffer=r"C:\Users\kursa\Desktop\homewok\04_Data_Analysis\imdb.csv",
)

#!Veri setimizin ilk 5 satırını gösterelim

# print(df.head().to_string()) #to string tamamını yazması için yazdık
# print(df.info())
# print(df.describe().to_string())
# print(df.shape)

#!movie title sütununun ilk 20 satırını gösterelim 
# #*path1
# print(df[["Movie_Title"]].head(20).to_string())

# #*path2
# print(df[["Movie_Title"]][0:20])

# #*path3
# print(df.loc[:20,"Movie_Title"])

#! 10-20. satır arası movie title ve  YR_Released getir
# print(df.loc[10:20, ["Movie_Title", "YR_Released"]])

#!rating 7.0'dan büyük olan filmlerin movie title,rating ve YR_Released sütunlarını gösterelim son olarak YR_Released sütununa göre azalan şekilde sıralayalım
# print(
#     df.query("Rating > 7.0")
#         .loc[:,["Movie_Title","Rating","YR_Released"]]
#         .sort_values(by="YR_Released",ascending=False)
# )

#!YR_Released 2014 ile 2018 arasında olan filmlerin Movie_Title, Rating ve YR_Released sütunlarını gösterelim ve Rating sütununa göre azalan şekilde sıralayalım

# print(
#     df.query("YR_Released > 2014 and YR_Released < 2018")
#       .loc[:, ["Movie_Title", "Rating", "YR_Released"]]
#       .sort_values(by="Rating", ascending=False)
# )

#!Num_Reviews 100000 'den büyük olab yada rating 8 ve 9 arasında olan filmlerin Movie_title ,Rating,YR_Released ve Num_Reviews sütunlarını gösterelim,Num_Reviews sütununa göre azalan şekilde sıralyalım


#?Path1
print(
    df[
        (df["Num_Reviews"] >= 100.000) | ((df["Rating"] >= 8)& (df["Rating"]<=9))
    ]
    [["Movie_Title","Rating","YR_Released","Num_Reviews"]]
    .sort_values(by="Num_Reviews" , ascending=False)
)

#?Path2
print(
    df.query("Num_Reviews>=100000 or Rating>=8 and Rating <=9")

        .loc[:, ["Movie_Title", "Rating", "YR_Released","Num_Reviews"]]
        .sort_values(by="Num_Reviews" , ascending=False)
    
    )