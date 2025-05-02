#!/usr/bin/env python3

import os
import sys

def check_if_armstrong_range(numbs: list):
    armstrong_numbers = []
    for number in numbs:
        total = 0
        num_digits = len(str(number))
        for digit in str(number):
            total += int(digit) ** num_digits
            if total > number:
                break
        if total == number:
            armstrong_numbers.append(number)
    return armstrong_numbers

def distribute_workload(max_range, processes):
    ranges = [[] for _ in range(processes)]
    for i in range(10, max_range + 1):
        ranges[i % processes].append(i)
    return ranges

def main():
    print("Welcome to the Armstrong number calculator.")
    try:
        top_range = int(input("Please enter the maximum number to calculate Armstrong numbers to (10 to 100,000,000): "))
        processes = int(input("Please enter the number of processes to use: "))
        if top_range < 10 or top_range > 100_000_000 or processes < 1:
            raise ValueError("Invalid input range or process count.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    workloads = distribute_workload(top_range, processes)
    child_pids = []

    for i in range(processes):
        pid = os.fork()
        if pid == 0:  # Child process
            armstrong_numbers = check_if_armstrong_range(workloads[i])
            print(f"Process {os.getpid()} found Armstrong numbers: {armstrong_numbers}")
            os._exit(0)
        else:  # Parent process
            child_pids.append(pid)

    for pid in child_pids:
        os.waitpid(pid, 0)

if __name__ == '__main__':
    main()