#fatwell
#28/10/24
#1201T3
Pass = input(":")
x = len(Pass)
FirstChar = ord(Pass[0:1])
LastChar  = Pass[(x-1):x]


while FirstChar > 90 or FirstChar < 65 or LastChar not in ["#", "$", "%"]:
    print("Please reenter the password as it is not sercure enough")
    Pass = input(":")
    x = len(Pass)
    FirstChar = ord(Pass[0:1])
    LastChar  = Pass[(x-1):x]
else:
    print("Pass is secure")
