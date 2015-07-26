
import time
import random


sheeps = random.randint(10, 100)
print("I can't sleep! it is", time.ctime(), "and I can't sleep!")
print("maybe if I try counting", sheeps, "jumping sheep!\n")
time.sleep(3)

medicine = ["Benadryl", "Lavender", "NyQuil", "Decaf"]
print("I have taken", medicine[random.randint(0, len(medicine)-1)], "and still nothing!")
print("I feel so tired and it is getting late, I better start counting!\n")
time.sleep(3)

zzzz = random.randint(1, 10)

i = 1
for x in range(0, zzzz):
    print(i, "sheep jumping over the fence!")

    if i >= zzzz-2:
        print("I'm so sleepy now, I'm barely making sense!")

    else:
        print("if I go over", sheeps/2, "this might get intense!")

    print("")
    i = i+1
    time.sleep(1)

print("zzzzzz...")