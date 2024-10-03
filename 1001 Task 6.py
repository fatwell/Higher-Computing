#3/10/24
#1001 Task 6
#Fatwell
from random import *

numbers = []

def random20numbers():
  for x in range(20):
    numbers.append(randrange(1,51))
  return numbers

def displayNumbers (numbers):
  for x in range(20):
    print  (numbers[x]," ",end="")

def findingMax(numbers):
  max = int(numbers[0])
  for i in range(20):
      if numbers[i] > max:
          max = int(numbers)
  print()
  print("The highest number (maximum) in the list is",max,".")

numbers = random20numbers()
displayNumbers(numbers)
findingMax(numbers)
