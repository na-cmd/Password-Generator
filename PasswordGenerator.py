import random
import time

lc_l = "abcdefghijklmnopqrstuvwxyz"
uc_l = lc_l.upper()
nums = "0123456789"
symbs = ",.<>/?;':\";:[]{}\\|[]}{!@#$%^&*()_+-="
elements = ""

print("Type in\"start\" to begin password generation process\n")
time.sleep(0.5)
print("-l - enables only lowercase letters\n")
time.sleep(0.5)
print("-u - enables only uppercase letters\n")
time.sleep(0.5)
print("-n - only numbers\n")
time.sleep(0.5)
x = input("-s - only symbols\n")
l = int(input("length:"))
a = int(input("Amount:"))

if x.find("start ") != -1:
    if x.find(" -l") != -1:
        elements += lc_l
    if x.find("-u") != -1:
        elements += uc_l
    if x.find("-n") != -1:
        elements += nums
    if x.find("-s") != -1:
        elements += symbs
elif x == "start":
    elements = lc_l + uc_l + nums + symbs

for y in range(a):
    pasw = "".join(random.sample(elements, l))
    print(pasw)
