f = open("firstfile.txt","r+")
data = f.read(10)
print(data)
f.close()