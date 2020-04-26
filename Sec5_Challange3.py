import csv

list1 = ["Top Gun", "Risky Business", "Minority Report"]
list2 = ["Ttanicc", "The Revenant", "nception"]
list3 = ["Training Day", "Man on Fire", "Flight"]

with open("movie.csv", "w", newline="") as f1:
    w = csv.writer(f1, delimiter=",")
    w.writerow(list1)
    w.writerow(list2)
    w.writerow(list3)
