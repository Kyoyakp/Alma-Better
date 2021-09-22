point = [[1,2],[1,1],[1.5,0]]
point.sort()
print(point)

# Output = [[1, 1], [1, 2], [1.5, 0]]

########################################################################################

point = [[1,2],[1,1],[1.5,0],0.6]
point.sort()
print(point)

# Output = TypeError: '<' not supported between instances of 'float' and 'list'
  
########################################################################################

point = [[1,2],[1,1],[1.5,0],['a','b']]
point.sort()
print(point)

# Output = TypeError: '<' not supported between instances of 'str' and 'int'
