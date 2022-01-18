#Largest palindrome product
'''A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''


def capicua(a):
    n = str(a)
    if n == n[::-1]:
        return True
    else:
        return False

n = 999
maior = 0
while n > 99:
    for i in range(100, 1000):
        a = n * i
        if a >= maior and capicua(a):
            maior =  a
    n -= 1
print(maior)

    


        
        
            


