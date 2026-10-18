def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    """
    A generator that yields prime numbers indefinitely.
    """
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# --- How to use the prime generator ---

# 1. Get a specific number of prime numbers:
print("First 10 prime numbers:")
primes = prime_generator()
for _ in range(10):
    print(next(primes))

print("\n--------------------\n")

# 2. Iterate through prime numbers up to a certain limit (less common for infinite generators, but possible):
print("Prime numbers less than 30:")
primes_up_to_30 = prime_generator()
for prime in primes_up_to_30:
    if prime >= 30:
        break
    print(prime)

print("\n--------------------\n")

# 3. Using a loop with a stopping condition (more typical for indefinite generators):
print("Prime numbers until you decide to stop (e.g., 5 prime numbers here):")
prime_gen = prime_generator()
count = 0
while count < 10:
    print(next(prime_gen))
    count += 1