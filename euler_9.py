'''

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
def triplet():
    for i in range(0,1001):
        for j in range(0,1001):
            for k in range(0,1001):
                if i<j and j<k and i*i+j*j == k*k and i+k+j == 1000:
                    prod = i*j*k
                    return prod

res = triplet()

print(res)
