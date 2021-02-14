#Print number after removing even number
num1= input("Enter an integer list(space separted):")
num=list(map(int,num1.split()))
num=[x for x in num if x%2!=0]
print("List after removing even number",end="")
print(num)
