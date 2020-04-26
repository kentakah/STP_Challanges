import csv

list1 = ["トップガン", "リスキービジネス", "マイノリティ・レポート"]
list2 = ["タイタニック", "レヴァナント", "インセプション"]
list3 = ["トレーニング・デイ", "マン・オン・ファイヤー", "フライト"]

with open("movie2.csv", "w", encoding="utf-8", newline="") as f1:
    w = csv.writer(f1, delimiter=",")
    w.writerow(list1)
    w.writerow(list2)
    w.writerow(list3)
