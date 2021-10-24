def remove_from_string(a , idx):
  a_ls = list(a)
  a_ls.pop(idx)
  a_ls.insert(idx, " ")
  return "".join(a_ls)

def compare(a, b):
  cows = 0
  bulls =0
  idx_cows = 0
  for x, y in zip(a, b):
    if x == y:
      cows +=1
      a = remove_from_string(a, idx_cows)
    elif y in a:
      bulls += 1
      idx_bulls = a.index(y)
      a = remove_from_string(a, idx_bulls)
    idx_cows += 1

  return f'cows: {cows}, bulls: {bulls}'

