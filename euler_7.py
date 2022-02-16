#10001st prime
'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. 
What is the 10 001st prime number?'''


#Obs:Not a super efficient resolution but it takes less than one minute to run
def primo(n):
  if n == 2:
      return True
  if n == 0 or n == 1:
      return False
  for i in range(2, n):
    if n % i == 0:
      return False
    else:
      continue
  return True


num = cont = 0

while True:
  if primo(num):
    cont += 1
  if cont == 10001:
    break
  num += 1
print(num)
   
