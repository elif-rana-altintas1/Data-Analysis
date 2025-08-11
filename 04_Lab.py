


import pandas as pd
df= pd.read_csv(
    filepath_or_buffer=r"C:\Users\kursa\Desktop\homewok\04_Data_Analysis\nba.csv",
)
print(df.head().to_string())


#!Takımlara göre maaş ortalaması nedir?

# result=df.groupby(by="Team")["Salary"].mean().sort_values(ascending=False)
# print(result)


#!en genç takımı bulunuz

# result=df.groupby(by="Team")["Age"].mean().sort_values(ascending=True).head(1)
# print(result)

#!İsmi içerisinde "and " ifadesi geçen oyuncular listesine ekleyelim


#?bu iş için custom bir fonksiyon yazalım

def player_find(name:str) -> bool:
    if "and" in name.lower():
        return True
    else:
        return False
    
result=df[
    df["Name"].apply (player_find)
] 
print(result[["Name","Team","Salary"]])

