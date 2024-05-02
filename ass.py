#for n multiple
n = int(input("Enter number:"))
while True:
    m = n*20
    if n<=m :
        print("Given number is greater than given number and multiple of 20")
        break
    else :
        print("Given number is lesser than given number and multiple of 20")
        break
print("num"+str(n))