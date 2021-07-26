#
#
#


f = open("Myfile.txt", "w")

f.write("Hello")
f.write(" ")
f.close()


f = open("MyFile.txt","a")
f.write("World")
f.write("\n")
f.close()

f = open("MyFile.txt", "r")
line = f.readline()
print(line)

print(line.strip("\n"))