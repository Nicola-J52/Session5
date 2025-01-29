# sum the first 10 numbers
sum = 0
for num in range(1,101): # 101 is excluded, so it goes from 1 to 100
    sum = sum +num
print(sum)

#rewrite it using while loop ^

sum = 0
num = 0
while num <= 100:
    num = num + 1
    sum+= num # same thing as sum = sum + 1

# print multiplication table
for i in range (1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")
    print() # to seperatr with a new line between blocks

i = 20
print("i i i ")
print(f"{i} {21+i} i i")

