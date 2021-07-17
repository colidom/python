# Using enumerate()funtion to find Python list max index
my_list =  [1, 220, 84, 43, 78]
max_item = max(my_list)
print([index for index, item in enumerate(my_list) if item == max_item])
