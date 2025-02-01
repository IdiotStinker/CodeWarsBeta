import math
input = ["100 7 DIVIDE 5.0", "7 7 MULTIPLY 49.0", "3 7 SUBTRACT 6.0", "3 7 ADD 12.0", "END"]
input = ["-33 9 SUBTRACT 22.0", "1 0 MULTIPLY 0.0", "1000 2000 ADD 4000.0", "-55 -5 DIVIDE 11.0","END"]
with open("prob03.txt", "r") as f:
    input = f.read().split("\n")
for thing in input:
    if thing == "END":
        break

    itemList = thing.split()
    itemOne = math.trunc(int(itemList[0]) * 10) / 10
    itemTwo = math.trunc(int(itemList[1]) * 10) / 10
    itemThree = math.trunc(int(itemList[3].split(".")[0]) * 10) / 10
    if itemList[2] == "DIVIDE":
        result = int(itemList[0]) / int(itemList[1])
        result = round(result * 10) / 10
        if not str(result) == itemList[3]:
            print(f"{itemOne} / {itemTwo} = {str(result)}, not {itemThree}")
        else:
            print(f"{itemThree} is correct for {itemOne} / {itemTwo}")
    
    if itemList[2] == "MULTIPLY":
        result = int(itemList[0]) * int(itemList[1])
        result = round(result * 10) / 10
        if not str(result) == itemList[3]:
            print(f"{itemOne} * {itemTwo} = {str(result)}, not {itemThree}")
        else:
            print(f"{itemThree} is correct for {itemOne} * {itemTwo}")
    
    if itemList[2] == "SUBTRACT":
        result = int(itemList[0]) - int(itemList[1])
        result = round(result * 10) / 10
        if not str(result) == itemList[3]:
            print(f"{itemOne} - {itemTwo} = {str(result)}, not {itemThree}")
        else:
            print(f"{itemThree} is correct for {itemOne} - {itemTwo}")

    if itemList[2] == "ADD":
        result = int(itemList[0]) + int(itemList[1])
        result = round(result * 10) / 10
        if not str(result) == itemList[3]:
            print(f"{itemOne} + {itemTwo} = {str(result)}, not {itemThree}")
        else:
            print(f"{itemThree} is correct for {itemOne} + {itemTwo}")