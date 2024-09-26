#804
#fatwell
#Step 1
totalWeight= 0
ContainerWeights = []
counter = 0
for i in range(5):
    ContainerWeight = int(input("What is the weight of food in the container: "))
    ContainerWeights.append(ContainerWeight)
    while ContainerWeight <0 or ContainerWeight > 200:
        print("Invalid, a single container can only hold up to 200g")
        ContainerWeight = input("What is the weight of food in the container: ")
    totalWeight += ContainerWeight
    
#Step 2
SizeDog = input("What size is your dog?(small, medium or large): ")

#Step 3
if SizeDog == "medium" and totalWeight > 330 and totalWeight < 440:
    WeightMessage = "The weight of food is suitable for your medium dog"

if SizeDog == "small" and totalWeight > 110 and totalWeight < 140:
    WeightMessage = "The weight of food is suitable for your small dog"

if SizeDog == "large" and totalWeight > 690 and totalWeight < 900:
    WeightMessage = "The weight of food is suitable for your large dog"

else:
    WeightMessage = "This weight of food is not recommended for the size of your dog"

#Step 4
AverageWeight = totalWeight/ 5
round(AverageWeight, 1)

#Step 5
for i in range(5):
    print(ContainerWeights[counter])
    counter += 1
print(totalWeight)
print(AverageWeight)
print(WeightMessage)

