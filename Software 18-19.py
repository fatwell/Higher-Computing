#2018-2019 assignment
#Finlay Atwell

from dataclasses import dataclass 
@dataclass
class Member:
    firstName: str = ''
    surname: str = ''
    distance: float = 0.0

def read_members():
    members = []
    with open("members.txt", 'r') as readfile:  
        for line in readfile:
            line = line.rstrip('\n')
            items = line.split(",")
            memberLocal = Member()
            memberLocal.firstName = items[0]
            memberLocal.surname = items[1]
            memberLocal.distance = float(items[2])  
            members.append(memberLocal)
    return members

def furthestDistance(membersArray):
    furthest = membersArray[0].distance
    for i in range(1,(len(membersArray))):
        if membersArray[i].distance > furthest:
            furthest = membersArray[i].distance
    return furthest
    
def prizewinners(membersArray, BiggestDistance):
    with open ("results.txt", "w") as wfile:
        wfile.write("The prize winning members are:" + "\n")
        for i in range(0, (len(membersArray))):
            if membersArray[i].distance > (0.7*BiggestDistance):
                wfile.write(membersArray[i].firstName + "," + membersArray[i].surname + "\n")
        wfile.write("The number of whole marathons walked by each member is:" + "\n")
        for i in range(0, (len(membersArray))):
            Marathons = int(membersArray[i].distance / 26.22)
            Marathons = str(Marathons)
            wfile.write(membersArray[i].firstName + "," + membersArray[i].surname + "," + Marathons + "\n")
        
            
members = read_members()
furthest = furthestDistance(members)
print(furthest)
prizewinners(members, furthest)




