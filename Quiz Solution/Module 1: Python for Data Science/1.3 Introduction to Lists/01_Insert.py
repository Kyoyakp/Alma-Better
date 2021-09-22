a = [10,23,56,[78,0,[1]]]
b = list(a)
a[1] = 34           # will not change b
b[0] = 19           # will not change a
a[3][0] = 95        # will change both
b[3][0] = 950       # will change both
b[3][2][0] = 5      # will change both
print(a)
print(b)
