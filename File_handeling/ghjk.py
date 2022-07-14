new = open("newspapers.txt","a")
new.write("mohanyadav")
b=new.readlines()
for i in b:
           li=list(i)
           print(li)
new.close()
    
