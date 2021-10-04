
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a() 

# My answer = after f
# Answer = error

# Output
'''
after f
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    a() 
  File "main.py", line 6, in a
    f(x, 4)
NameError: name 'f' is not defined
'''
