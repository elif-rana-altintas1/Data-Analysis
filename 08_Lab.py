

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Excel dosyasını oku
df_can = pd.read_excel(
    r"C:\Users\kursa\Desktop\homewok\04_Data_Analysis\Canada.xlsx",
    sheet_name="Canada by Citizenship",
    skiprows=range(20),
    skipfooter=2
)

# Bilgi çıktısı
print(df_can.info())

# Sütunları yeniden adlandır (VİRGÜL EKSİĞİ GİDERİLDİ)
df_can.rename(
    columns={
        "OdName": "Country",
        "AreaName": "Continent",
        "RegName": "Region"
    },
    inplace=True
)

# Gereksiz sütunları sil
df_can.drop(
    columns=["AREA", "REG", "Type", "Coverage", "DevName", "DEV"],
    axis=1,
    inplace=True
)



df_can.columns =list(
    map(str, df_can.columns)
) 

df_can.set_index(
    keys="Country",
    inplace=True

)

years = list (map(str , range(1980,2014)))
#* total adında yeni sütun oluşturduk ve veri setinde yıl yıl göçmen miktaralarını toplayarak üzerine yazdık
df_can["total"] = (
    df_can.sum(
        axis=1 ,
          numeric_only=True
          )
   )
#* veri setimizi total sütünun agöre çoktan aza sıraladık
df_can.sort_values(
    by="total",
    ascending=False,
    inplace=True

)
#*En çok göç vermiş 5 ülke 
df_top_5_country = df_can.head()
df_top_5_country=df_top_5_country[years].transpose()

#* en .ok göç vermiş 5 ülkenin alan grafiğini yapalım.
# df_top_5_country.plot(
#     kind="area",
#     stacked=False,
#     figsize=(10,7),
#     alpha=0.25

# )


# plt.title(label="Immigrant Trend of Top 5 Countries", fontsize=16, color="red")
# plt.xlabel(xlabel="Years", fontsize=13, color="red")
# plt.ylabel(ylabel="Number of Immigrants", fontsize=13, color="red")
# plt.show()


#* 2013 yılındaki göçmen hareketliliğini histogram grafiğinde verelim
# count, bin_edges = np.histogram(df_can["2013"])

# # Histogram çizimi
# df_can["2013"].plot(
#     kind="hist",
#     figsize=(10, 7),
#     xticks=bin_edges,
#     color="b"
# )

# # Grafik başlıkları ve etiketler
# plt.title(label="Histogram of Immigrants from 2013", fontsize=16, color="red")
# plt.xlabel(xlabel="Number of Immigrants", fontsize=13, color="red")
# plt.ylabel(ylabel="Number of Countries", fontsize=13, color="red")

# plt.grid(True)

# plt.show()



#* 1980-2013 yılları arasındaki iceland göçmenlerini çubuk grafikte gösterelim 
# df_iceland = df_can.loc["Iceland",years]

# df_iceland.plot(
#     kind="bar",
#     figsize=(10,7)

# )

# plt.title(label="Iceland Immıgrant of canada",fontsize=16,color="red")
# plt.xlabel(xlabel="Years",fontsize=13,color="red")
# plt.ylabel(ylabel="Number of Immigarnt",fontsize=13,color="red")
# plt.grid(True)
# plt.show()

df_continents = df_can.groupby(by="Continent").sum()

df_continents["total"].plot(
    kind="pie",
    figsize=(10,7)
    startangle=90,
        autopct='%1.1f%%',
    labels=None,
    shadow=True,
    explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    pctdistance=1.1
)

plt.axis('equal')  # Dairenin yuvarlak görünmesi için

plt.legend(
    labels=df_continents.index,
    prop={
        'size': 8
    }
)

plt.show()
