name=open("village_boys_data.txt","a")
for i in range(2):
    z=input("enter the boys names and age")
    name.write(z)
    name.write("\n")
name.close()
name=open("village_boys_data.txt","r")
data=name.readlines( )
print(data)
#b=name.split(" ")
#print(data.split(" "))
n=[]
h = []
for i in data():
    val = i.split(" ")
    print(val)
    #n.append(val[0])
    #h.append(val[1])
#print(n)
#print(h)
name.close()

    




    
