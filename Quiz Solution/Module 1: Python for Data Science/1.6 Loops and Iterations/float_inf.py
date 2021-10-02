for i in range(int(float('inf'))):
    print (i)
    
# output - OverflowError: cannot convert float infinity to integer

print(int(float('inf')))

# output - OverflowError: cannot convert float infinity to integer

print(float('inf'))

# output - inf

print(float('inft'))

# output - ValueError: could not convert string to float: 'inft'

