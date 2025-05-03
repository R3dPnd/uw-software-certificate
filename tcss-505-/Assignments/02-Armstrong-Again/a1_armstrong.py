#!/usr/bin/env python3

import os
import time
import argparse
import pickle

def is_armstrong(n):
    # Convert number to string to get digits
    digits = str(n)
    # Get number of digits
    num_digits = len(digits)
    # Calculate sum of digits raised to power of number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    # Check if sum equals original number
    return sum_of_powers == n

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

def print_armstrong_numbers(numbers, process_id):
    print(f"Child process PID:{process_id} found: {numbers}")

def main():

    print("Welcome to the Armstrong number calculator.")
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Find Armstrong numbers using multiple processes')
    parser.add_argument('-n', '--number', type=int, help='Upper limit for Armstrong number search')
    parser.add_argument('-p', '--processes', type=int, help='Number of processes to use')
    args = parser.parse_args()

    # Get parameters from command line or user input
    if args.number is None:
        number_limit = int(input("Please enter the maximum number to calculate Armstrong numbers to (10 to 100,000,000): "))
    else:
        number_limit = args.number

    if args.processes is None:
        num_processes = int(input("Please enter the number of processes to use: "))
    else:
        num_processes = args.processes

    # Calculate numbers per process
    numbers_per_process = number_limit // num_processes
    print(f"Numbers per process: {numbers_per_process}")

    # Start timing
    start_time = time.time()

    # Create a list to store process IDs and pipes
    pids = []
    pipes = []

    # Create processes
    for i in range(num_processes):
        # Create a pipe for this process
        read_pipe, write_pipe = os.pipe()
        pipes.append((read_pipe, write_pipe))

        pid = os.fork()
        if pid == 0:  # Child process
            # Close the read end of the pipe in child
            os.close(read_pipe)

            start = i * numbers_per_process + 1
            end = (i + 1) * numbers_per_process if i < num_processes - 1 else number_limit
            
            # Find Armstrong numbers for this process's range
            armstrong_numbers = find_armstrong_numbers(start, end)
            
            # Print numbers found by this process
            print_armstrong_numbers(armstrong_numbers, i + 1)
            
            #Write results to pipe
            with os.fdopen(write_pipe, 'wb') as pipe:
                pickle.dump(armstrong_numbers, pipe)
            
            os._exit(0)  # Exit child process
        else:  # Parent process
            # Close the write end of the pipe in parent
            os.close(write_pipe)
            pids.append(pid)

    # Wait for all child processes to complete
    all_armstrong_numbers = []
    for i, (read_pipe, _) in enumerate(pipes):
        os.waitpid(pids[i], 0)
        # Read results from pipe
        with os.fdopen(read_pipe, 'rb') as pipe:
            numbers = pickle.load(pipe)
            all_armstrong_numbers.extend(numbers)

    # Calculate and print runtime
    end_time = time.time()
    runtime = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"It took {runtime:.2f} milliseconds to complete the task")

    print(f"Armstrong numbers found: {str(all_armstrong_numbers).strip('[]')}")

if __name__ == "__main__":
    main()