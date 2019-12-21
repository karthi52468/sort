def s(alist):
    m=alist[0]
    if(len(alist)>1):
       for j in range(len(alist)-1):
           if(m>alist[j+1]):
               m=alist[j+1]
       return m
    else:
       return m
alist=[]
alist=input("Enter the numbers : ").split()
alist=list(map(int,alist))
b=[]
for i in range(len(alist)):
       d=s(alist)
       b.append(d)
       alist.remove(d)
print("Accending order : ")
for x in b:
    print(x)
b=b[::-1]
print("Decending order :")
for x in b:
    print(x)
