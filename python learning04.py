
pwd_correct = True

if pwd_correct :#condition stmp
    print("have a nice day")
    print("all the best")
else:
    print("bad day")
    print("all the worst for you")

print( "hi")

english = int(input("english :"))
tamil = int(input("tamil :"))
math = int(input("maths :"))
physics = int(input("physics :"))
chemistry = int(input("chemistry :"))
computer = int(input("computer :"))
if english > 100 or tamil > 100 or math > 100 or physics > 100 or chemistry > 100 or computer > 100 :#condition stmp
    print("invalid mark")
else:
    if english >= 35 and tamil >= 35 and math >=35 and physics >= 45 and chemistry >= 45 and computer >= 45 :#condition stmp
        print("promotted")
    else:
        print("depromotted")
total = english + tamil + math + physics + chemistry + computer
print("Total : " + str(total))
