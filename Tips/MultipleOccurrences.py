# Finding max index for multiple occurrences of elements
my_list =  [1, 220, 84, 43, 78, 220]
max_item = max(my_list)
index_list = [index for index in range(len(my_list)) if my_list[index] == max_item]

print(index_list)
