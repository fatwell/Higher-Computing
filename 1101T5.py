#1101T5
#9/10/24
#fatwell
Temperatures = []
total = 0
with open("Temperatures.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        print(items)
        Temperatures.append(items[1])
        print(Temperatures)
        line = readfile.readline().rstrip('\n')

for i in range(len(Temperatures)):
    total+= Temperatures[i]
    print(total)

AverageTemp = float(total/(len(Temperatures)))
print(AverageTemp)

    
    
