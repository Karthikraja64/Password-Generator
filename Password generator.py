#CODED BY KARTHIK RAJA


print("PASSWORD GENERATOR BY KARTHIK RAJA")




import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "{}[]()@#"

ans = upper_case + lower_case + num + special

length = input("password length : ")

password = "".join(random.sample(ans,length))

print("Your Generated Password is ",password)

#CODED BY KARTHIK RAJA