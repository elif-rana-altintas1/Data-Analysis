
import pandas as pd
df= pd.read_csv(
    filepath_or_buffer=r"C:\Users\kursa\Desktop\homewok\04_Data_Analysis\youtube-ing.csv",
)
print(df.head())

print(df.info())

#!En çok görüntülenme(views) almış 10 farklı videonun title ve views sütunlarını gösterelim ve viewa göre sort edelim
# result=(
#     df.groupby(by="title")
#     .agg({
#         "views" :"sum"

#     })
#     .sort_values(by="views",ascending=False)
#     .head(10)
# )
# print(result)

#! category_idsine göre like ortalamasını bulalım.
# result=(
#     df.groupby(by="category_id")
#     .agg({
#         "likes" :"mean"

#     })
#     .sort_values(by="likes",ascending=False)
#     .query("likes >101695.733333")
#     .head(10)
# )
# print(result)


#*Her bir video için kullanılan tag sayısını hesaplayan bir fonksiyon yazalım ve elde ettiğimiz değerleri "tag_count " isimli yeni bir sütuna ekleyelim.

# #?path1
# def calculate_tag_count(tags: str) -> int:
#     return len(tags.split("|"))

# df["tag_count"] = df["tags"].apply(calculate_tag_count)

# print(df[["title", "tag_count"]].sort_values(by="tag_count", ascending=True))

# #? path2
# df["tag_count"]= df["tags"].apply(lambda x : len (x.split("|")))

#* her bir videonun like ve dislike oranını hesaplayalım ve "like_dislike_ratio" isimli yeni bir sütuna ekleyelim

def like_dislike_ratio(data_set: pd.DataFrame) -> list:
    like_list= list(data_set["likes"])
    dislike_list=list(data_set["dislike"])

    combined_list = list(
        zip(like_list,dislike_list)
    )
    average_list=list()

    for like,dislike in combined_list:
        if like + dislike ==0:
            average_list.append(0)

        else:
            average_list.append(like/ (like + dislike)) 

    return average_list

df["like_dislike_ratio"]=like_dislike_ratio(df)
print(df[["title","like_dislike_ratio"]].sort_values(by="like_dislike_ratio",ascending=False).head(10))