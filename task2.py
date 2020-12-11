#1
x=str(input("Enter the string:"))
print(x[-1]+x[1:]+x[0])

#2
a=input("Enter a string: ")
c=input("enter the length of 0's:")
b=int(c)
d = c.zfill(b)
print(d[:-1]+'0'+a)

temp = str(input("Enter the string : "))
tlen=len(temp)
zlen = int(input("Enter the number of zeros : "))
x = tlen+zlen
x = temp.zfill(x)
print(x)


#3
x=str(input("Enter the string: "))

def ss():
    y=int(input("Enter the first position: "))
    z=int(input("Enter the last position: "))
    l=[]
    for i in range(y-1,z):
        s=str(i)
        l.append(s)
    print(x[:y-1]+x[z:])
