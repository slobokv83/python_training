# keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)

numbers2['x'] = 10
numbers2['t'] = 'bla'

print('numbers2 =',numbers2)