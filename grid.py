l = 'aaabbaabccdde'

l1 = {}
z = ''

for i in l:
  if i not in l1:
    l1[i] = 1
    temp = i
    flag = True
  elif (flag):
    if (i != temp):
      flag = False
    else:
      l1[i] += 1

for x, y in l1.items():
  z += x + str(y)

print(z)