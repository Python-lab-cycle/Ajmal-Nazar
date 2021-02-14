str1 = input("enter a first string:")
str2 = input("enter a second string:")
new_a = str2[:1] + str1[1:]
new_b = str1[:1] + str2[1:]
print("the new string after swapping first two character of both strings :",(new_a+' '+new_b))
