#input = [1111, 21, 12132, 10231122013, 122230333000, "000"]
input = []
with open("prob06.txt", "r") as f:
    inputReal = f.read().split("\n")

for thing in inputReal:
    input.append(int(thing))

for num in input:
    if num == 0:
        break
    total = 0
    for i in range(len(str(num)), 0, -1):
        
        total += int(str(num)[i-1]) * (4**(len(str(num))-i))
        #print(total)

    print(total)