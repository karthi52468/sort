def s(alist):
    m=alist[0]
    if(len(alist)>1): 
       for j in range(len(alist)-1):
           if(m>alist[j+1]): 
               m=alist[j+1] # getting the small value from the list and return to main function
       return m
    else:
       return m
alist=[] #creating a empty list
alist=input("Enter the numbers : ").split() # split the list by space 
alist=list(map(int,alist))
b=[]
for i in range(len(alist)): # creating a loop for getting value to list using append in build function
       d=s(alist)#caliing function
       b.append(d) #adding the value to another listwhich is sent by function
       alist.remove(d)#delete the value in main list
        # loop repeated till the list come to the last index
print("Accending order : ")
for x in b:
    print(x)
b=b[::-1]
print("Decending order :")
for x in b:
    print(x)
