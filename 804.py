#804
#fatwell
#Step 1

def valid_food_weight():
    totalWeight= int(0)
    ContainerWeights = []
    for i in range(5):
        ContainerWeight = int(input("What is the weight of food in the container: "))
        ContainerWeights.append(ContainerWeight)
        while ContainerWeight <0 or ContainerWeight > 200:
            print("Invalid, a single container can only hold up to 200g")
            ContainerWeight = int(input("What is the weight of food in the container: "))
        totalWeight += ContainerWeight
    return totalWeight, ContainerWeights
    
#Step 2
def size_of_dog():
    SizeDog = input("What size is your dog?(small, medium or large): ")
    return SizeDog

#Step 3
def ReccomendationMessage(SizeDog, totalWeight):
    
    if SizeDog == "medium" and totalWeight > 330 and totalWeight < 440:
        WeightMessage = "The weight of food is suitable for your medium dog"
    elif SizeDog == "small" and totalWeight > 110 and totalWeight < 140:
        WeightMessage = "The weight of food is suitable for your small dog"
    elif SizeDog == "large" and totalWeight > 690 and totalWeight < 900:
        WeightMessage = "The weight of food is suitable for your large dog"
    else:
        WeightMessage = "This weight of food is not recommended for the size of your dog"
    return(WeightMessage)

#Step 4
def Average_Weight(totalWeight):
    AverageWeight = totalWeight/ 5
    return(round(AverageWeight, 1))

#Step 5
def OutputMessages(totalWeight, AverageWeight, WeightMessage):
    for i in range(5):
        print(ContainerWeights[i])
    print(totalWeight)
    print(AverageWeight)
    print(WeightMessage)

# main program
totalWeight, ContainerWeights = valid_food_weight()
SizeDog = size_of_dog()
WeightMessage = ReccomendationMessage(SizeDog, totalWeight)
AverageWeight = Average_Weight(totalWeight)
OutputMessages(totalWeight, AverageWeight, WeightMessage)
