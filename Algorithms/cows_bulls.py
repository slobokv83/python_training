import random

print('\n***********************************************')
print('***** Welcome to the Cows and Bulls Game! *****')
print('***********************************************\n')
print('Please enter the number of digits you want to guess:')
num_digits = int(input())

def remove_from_string(a , idx):
  a_ls = list(a)
  a_ls.pop(idx)
  a_ls.insert(idx, "*")
  return "".join(a_ls)

def compare(a, b):
  cows = 0
  bulls =0
  idx_cows = 0
  for x, y in zip(a, b):
    if x == y:
      cows +=1
      a = remove_from_string(a, idx_cows)
    idx_cows += 1
  for y in b:
    if y in a:
      bulls += 1
      idx_bulls = a.index(y)
      a = remove_from_string(a, idx_bulls)
  return cows, bulls

guess_number = ""
for i in range(num_digits):
  guess_number += str(random.randint(0, 9))
while True:
  print(f'Enter a number [{num_digits} digits]:')
  your_guess = input()
  print('')

  if len(your_guess) != num_digits:
    print(f'Please enter {num_digits} digits number!')
    print('-----------------------------------')
  else:
    # print('The guess number: ', guess_number)
    cows, bulls = compare(guess_number, your_guess)
    if cows == num_digits:
      print('Congratulation!')
      break
    else:
      print(f'= cows: {cows}, bulls: {bulls}')
      print('-----------------------------------')
  