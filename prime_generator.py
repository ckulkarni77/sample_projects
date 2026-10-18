def is_prime(f_num):
    if f_num<2:
        return False
    for _ in range(2,int(f_num**0.5) + 1):
        if f_num % _ == 0:
            return False
def generate_prime():
    count=2
    while True:
        if is_prime(count):
            yield count
        count+=1

primes =  generate_prime()       
for _ in range(20):
    print(next(primes))