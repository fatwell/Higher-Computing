from dataclasses import dataclass
heights = [1.75, 1.62, 1.88, 1.7, 1.8]
weights = [70.5, 55.8, 95.2, 82.3, 66]
counter = int(0)
@dataclass

class person():
  height : float = 0.0
  weight : float = 0.0
  bmi : float = 0.0

BMIrecord = [person() for index in range(40)]
for i in range(5):
  BMIrecord[counter].height  = heights[counter]
  BMIrecord[counter].weight  = weights[counter]
  BMIrecord[counter].bmi = BMIrecord[counter].weight / (BMIrecord[counter].height ** 2)
  print(BMIrecord[counter])
  counter += 1

