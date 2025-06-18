def is_prime(f_num):
    for n in range(2,99):
        if f_num%n == 0:
            return False
        
def gen(f_num):
    if is_prime(f_num):
        yield f_num
            
for n in range(2,50):
    print(next(gen(n)))

