with open("prob05.txt", "r") as f:
    inputReal = f.read()

splitChar = inputReal.split("\n")[0]
string = inputReal.split("\n")[1]
#print(string)
splitNum = string.index(splitChar)

after = string[splitNum + 1:]

before = string[:splitNum]


list(after).reverse()

print(after + splitChar + before)