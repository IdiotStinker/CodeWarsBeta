with open("prob08.txt", "r") as f:
    j = f.read()
    lines = j.split("\n")

numOfLines = int(lines[0][0]) + 1
lines[0] = " "

newLines = []
for i in range(numOfLines):
    newLines.append([])

for l, line in enumerate(lines):
    newLines[numOfLines - l -1] = line

for line in newLines:
    print(line)
