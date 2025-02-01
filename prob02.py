input = [2, 4, 6, 22, -18, 90, 102, 0]
with open("input.txt", "r") as f:
    f = f.read()
    j = f.split("\n")

for thing in j:
    input.append(int(thing))

even = True
for thing in input:
    if thing % 2 == 0:
        continue
    else:
        even = False
        print(f"{thing} is odd")

if even:
    print("FLASH FORWARD")
else:
    print("FLASH FAILED")