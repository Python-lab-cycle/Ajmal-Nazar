file1=input("Enter the source file to be copied:")
file2=input("Enter the destination file name:")
f1=open(file1,"r")
f2=open(file2,"w")
for line in f1.readlines():
    f2.write(line)
f2.close()
f1.close()
print("1 File Copied")
