#fatwell
#28/10/24
#1201T2
word = input("Enter the name of an animal: ")
Final = len(word) 
FirstLetter = chr(ord(word[0:1]) - 32)
EndWord = word[1:Final]
word = FirstLetter+EndWord
print(word)
