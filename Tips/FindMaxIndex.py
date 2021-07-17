# Using for loop
my_list =  [1, 220, 84, 43, 78]
max = my_list[0]
index = 0

for i in range(1, len(my_list)):
    if my_list[i] > max:
        max = my_list[i]
        index = i
print(f"Max index is: {index}")
