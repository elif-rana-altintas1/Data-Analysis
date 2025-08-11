
import pandas as pd

#! Merge1
# İki DataFrame’i birleştirmek/merge yapmak için merge() fonksiyonu kullanılır.
# SQL’deki join işlemiyle çok benzer şekilde çalışır.
# Kodda merge işlemi için DataFrame’lerde ortak sütun olması gerekir. Örnek vermek gerekirse, her iki DataFrame'de de "id"
# sütunu varsa bu sütun üzerinden merge işlemi yapılabilir.
# Bu işlemi yapmak için merge() fonksiyonunu kullanarak gerçekleştirebiliriz.
# İçeriden birleşim türleri (join türleri) belirtilebilir.
# Kodda "left merge" işlemi ise, sol DataFrame'deki tüm satırları alır ve sağ DataFrame'deki eşleşen satırları ekler. Eğer
# sağ DataFrame'de eşleşen satır yoksa, NaN değerleri ile doldurur.


customers = {
    'customer_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 40, 22]
}

orders = {
    'order_id': [101, 102, 103, 104, 105, 106],
    'customer_id': [1, 2, 4, 5, 6, 1],
    'product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Keyboard', 'Mouse'],
    'quantity': [4, 2, 1, 1, 3, 2]
}

customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)

#! Inner merge işlemi
# result = pd.merge(
#     left=customers_df,
#     right=orders_df,
#     how="inner",
#     on="customer_id"
# )

# print(result)

#! Right merge
result = pd.merge(
    left=customers_df,
    right=orders_df,
    how="right",
    on="customer_id"
)
print(result)