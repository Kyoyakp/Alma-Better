lst = [3,4,6,1,2]
lst[2] = [7,8,9,10]
print(lst)

# Output = [3, 4, [7, 8, 9, 10], 1, 2]

lst = [3,4,6,1,2]
lst[1:2] = [7,8,9,10]
print(lst)

# Output = [3, 7, 8, 9, 10, 6, 1, 2]

lst = [3,4,6,1,2]
lst[1:4] = [7,8,9,10]
print(lst)

# Output = [3, 7, 8, 9, 10, 2]

lst = [3,4,6,1,2]
lst[:2] = [7,8,9,10]
print(lst)

# Output = [7, 8, 9, 10, 6, 1, 2]

lst = [3,4,6,1,2]
lst[2:] = [7,8,9,10]
print(lst)

# Output = [3, 4, 7, 8, 9, 10]

lst = [3,4,6,1,2]
lst[:] = [7,8,9,10]
print(lst)

# Output = [7, 8, 9, 10]








