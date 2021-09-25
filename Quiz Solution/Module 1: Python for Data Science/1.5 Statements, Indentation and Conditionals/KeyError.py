# The following if/elif/else statement will raise a KeyError exception:
 
d = {'a': 0, 'b': 1, 'c': 0}
 
if d['a'] > 0:
    print('ok')
elif d['b'] > 0:
    print('ok')
elif d['c'] > 0:
    print('ok')
elif d['d'] > 0:
    print('ok')
else:
    print('not ok')
    
'''False: Since "elif d['d'] > 0:" will not exicute ///// 'ok' will be printed by "elif d['b'] > 0:"  '''
