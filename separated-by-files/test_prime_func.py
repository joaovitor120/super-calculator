import math

def isprime(num):
    if num < 2:
        return False
    for i in range(2, (int(math.sqrt(num))) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Type a num: "))
prime_status = isprime(num)
if prime_status == True:
    print(f"{num} is a prime number!")
else: 
    print(f"{num} isn't a prime number. ")