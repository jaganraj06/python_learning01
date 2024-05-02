#print5table
num=1
while num<=20:
    print(num*5)
    num=num+2


#print the factors of n
n=int(input("enter any number:"))
print("the factor of", n ,"are")
for i in range(1,n+1):
    if n % i== 0:
         print (i)



