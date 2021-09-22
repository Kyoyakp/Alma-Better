a = [10,23,56,[78,0,[1]]]
b = list(a)
a[1] = 34           # will not change b
b[0] = 19           # will not change a
a[3][0] = 95        # will change both
b[3][0] = 950       # will change both
b[3][2][0] = 5      # will change both
print(a)
print(b)

# output = [10, 34, 56, [950, 0, [5]]]
#          [19, 23, 56, [950, 0, [5]]]

#############################################################################################

# If the way of assining the list change the output becomes same.
a = [10,23,56,[78,0,[1]]]
b = a
a[1] = 34           
b[0] = 19           
a[3][0] = 95        
b[3][0] = 950       
b[3][2][0] = 5      
print(a)
print(b)

# output =[19, 34, 56, [950, 0, [5]]]
#         [19, 34, 56, [950, 0, [5]]]