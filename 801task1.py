from dataclasses import dataclass

@dataclass

class person():
  height : float = 0.0
  weight : float = 0.0
  bmi : float = 0.0

BMIrecord = [person() for index in range(40)]

BMIrecord[0].height  = 1.75
BMIrecord[0].weight  = 70.5
BMIrecord[0].bmi = BMIrecord[0].weight / (BMIrecord[0].height ** 2)

BMIrecord[1].height  = 1.62
BMIrecord[1].weight  = 55.8
BMIrecord[1].bmi = BMIrecord[1].weight / (BMIrecord[1].height ** 2)

BMIrecord[2].height  = 1.88
BMIrecord[2].weight  = 95.2
BMIrecord[2].bmi = BMIrecord[2].weight / (BMIrecord[2].height ** 2)

BMIrecord[3].height  = 1.7
BMIrecord[3].weight  = 82.3
BMIrecord[3].bmi = BMIrecord[3].weight / (BMIrecord[3].height ** 2)

BMIrecord[4].height  = 1.8
BMIrecord[4].weight  = 66
BMIrecord[4].bmi = BMIrecord[4].weight / (BMIrecord[4].height ** 2)

print(BMIrecord[0])
print(BMIrecord[1])
print(BMIrecord[2])
print(BMIrecord[3])
print(BMIrecord[4])



