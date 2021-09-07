a = [[1,2,3,4,5],[1,6,7,3,2,8,4],[1,9,3,10,2,11,4],[2,12,13,14,3,4,5],\
[1,15,16,2,17,3,5],[1,18,2,19,3,20]]

def common(a):
  dict1 = {}
  for i in a[0]:
    dict1[i] = 1
    for j in a[1:]:
      if i in j:
        dict1[i] += 1

   
  print([key  for (key, value) in dict1.items() if value == len(a)])

common(a)