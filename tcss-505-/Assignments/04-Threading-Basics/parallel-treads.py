#!/usr/bin/env python3

# Write a program (Python or C or ?) that uses at least two threads to execute the same code (function/method) with the goal 
# of improving the performance of the code. First execute the program with a single thread and time the result. Next, execute 
# the program with more than one thread and time the result showing an improvement in performance. Note that depending on the 
# problem you decide to solve, you may (will?) find that a single thread performs better if your algorithm works with a small 
# range of parameters/values. A possible task you might try and perform is to produce prime numbers in a certain range. 
# There are many examples you can borrow from to do this. You could assign each thread a particle range to calculate and then 
# bring the results together (via a join from your main thread).

import threading
import time

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# Function to find primes in a given range and store them in the result list
# simple implementation 
def find_primes(start, end, result):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)

# Create a single-thread calling te find_primes function
def single_threaded_prime_search(start, end):
    result = []
    find_primes(start, end, result)
    return result

# Create a multi-threaded version of the prime search
def multi_threaded_prime_search(start, end, num_threads=2):
    threads = []
    results = [[] for _ in range(num_threads)]
    step = (end - start) // num_threads
    for i in range(num_threads):
        s = start + i * step
        e = start + (i + 1) * step if i != num_threads - 1 else end
        t = threading.Thread(target=find_primes, args=(s, e, results[i]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    # Flatten results
    primes = []
    for r in results:
        primes.extend(r)
    return primes

if __name__ == "__main__":
    START = 1_000_000
    END = 5_000_000
    print(f"Searching for primes between {START} and {END}...")

    print("Single-threaded execution:")
    t1 = time.time()
    primes_single = single_threaded_prime_search(START, END)
    t2 = time.time()
    print(f"Found {len(primes_single)} primes in {t2 - t1:.4f} seconds.")

    print("\nMulti-threaded execution (4 threads):")
    t3 = time.time()
    primes_multi = multi_threaded_prime_search(START, END, num_threads=4)
    t4 = time.time()
    print(f"Found {len(primes_multi)} primes in {t4 - t3:.4f} seconds.")

    # Optional: Check that both methods found the same primes
    print("\nResults are identical:", sorted(primes_single) == sorted(primes_multi))