num_int = 1
num_float = 2.45
strg = 'Kaca' 
tup = (1,2,3,4,5,6)
set1 = {'apple', 'orange', 'mango'}
dict1 = {'Kaca': 'plava', 'Lenka': 'plava', 'Suzana': 'plava', 'Slobodan': 'pametan'}
arr = [1,2,3,4,5,6]

## tuple
# def pamet(x):
#     x = x + (7,)
#     return x
# v = pamet(tup)
# print('value: ', tup)
# print(v)

## num_int
# def pamet(x):
#     x = x + 5
#     return x

# v = pamet(num_int)
# print('value: ', num_int)
# print(v)

## num_float
# def pamet(x):
#     x = x + 5
#     return x

# v = pamet(num_float)
# print('value: ', num_float)
# print(v)

## strg
# def pamet(x):
#     x = x + ' je najbolja!'
#     return x

# v = pamet(strg)
# print('value: ', strg)
# print(v)

## set
# def pamet(x):
#     x = x.add(' je najbolja!')
#     return x

# v = pamet(set1)
# print('reference: ', set1)
# print(v)

## dict
# def pamet(x):
#     x['Suzana'] = 'pametna'
#     return x

# print('reference: ', dict1)
# v = pamet(dict1)
# print('reference: ', dict1)
# print(v)

## array
def pamet(x):
    x[2] = 8
    return x

print('reference: ', arr)
v = pamet(arr)
print('reference: ', arr)
print(v)