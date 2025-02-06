import csv
thisDate = []
country = []
location = []
shape = []
description = []
filePath = ''  

# -------------------------------------------------- DO NOT ALTER -----
def importFile():
    with open(filePath + 'ufo_sighting.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip header row if present
        for row in reader:
            thisDate.append(row[0])
            country.append(row[1])
            location.append(row[2])
            shape.append(row[5])
            description.append(row[6])
    return thisDate, country, location, shape, description
# -------------------------------------------------- DO NOT ALTER -----

def countPerCountry(countryarray, specifiedcountry):
    numSightings = 0
    for i in range(len(countryarray)):
        if countryarray[i] == specifiedcountry:
            numSightings += 1
    return numSightings

def displaySightings(specifiedcountry, numSightings):
    print("There are", numSightings, "sightings that took place in", specifiedcountry)

def countyearsightings(thisDate):
    year_sightings = 1
    for i in range(0, len(thisDate) -1):
        currentyear = thisDate[i][6:10]
        nextyear= thisDate[i+1][6:10]
        if currentyear == nextyear:
            year_sightings = year_sightings + 1
        else:
            print(currentyear, year_sightings)
            year_sightings = 0

def specifiedLocation(location, thisDate, shape, description):
    Found = False
    spflocation = input("Please enter a specific Locaiton: ")
    for i in range(len(location)):
        if spflocation == location[i]:
            print(f"{thisDate[i]}, {shape[i]}, {description[i]}")
            Found = True
    if Found == False:
        print("No sighgtings were found in your desired location")
    
# Main program
specifiedcountry = ["England", "Scotland", "Wales", "Northern Ireland"]
thisDate, country, location, shape, description = importFile() 
for index in specifiedcountry:
    numSightings = countPerCountry(country, index)  
    displaySightings(index, numSightings)

countyearsightings(thisDate)
specifiedLocation(location, thisDate, shape, description)
