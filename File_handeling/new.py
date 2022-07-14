data = open("myvillage.txt","r")
info  =  data.readlines()
for i in info:
    li = i.split(" ")
    name = li[0]
    degree = li[1]
    print(name)
    print(degree)
data.close()
