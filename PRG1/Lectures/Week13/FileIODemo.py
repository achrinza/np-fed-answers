import os

f = open("test.txt" "w")

list1 = ["Shoes", "Socks", "Gloves"]
quantity = [10, 5, 32]

f.write("{:<10} {:10} {:10}\n".format("S/N", "Items", "Quantity"))

for item in list1:
    f.write("{:<10} {:10} {:10}\n".format("S/N", "Items", "Quantity") + "\n")

f.close()