#delimited by comma
str_ip="234,224,117,175,543"
str2 =[]
str3 =''
for i in str_ip:
    if i==',':
        str2.append(int(str3))
        str3=""
        continue
    else:
        str3=str(str3)+str(i)
print(str2)

newlist=str_ip.split(',')
#split
print(newlist)
#join
print("-".join(newlist))

