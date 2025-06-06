#!/usr/bin/env python3
import threading
import time
import random

# Write a program (Python or C or ?) that uses at least two threads to access the same data. 
# At least one thread should read the data and at least one thread should modify the data. 
# First run the program with no protection in place for the data and capture the output (which should show 'messiness'). 
# Next, add protection to the data (a lock or something to synchronize) so that a thread that wants to read the data 
# cannot access that data while a thread that is modifying the data is active. 
# A possible task you might try and perform is to read from a file and write to that same file. 
# You could do the same thing with a data structure of some form. Or?

# Shared data 
shared_data = -1

def reader():
    global shared_data
    for _ in range(10):
        # Simulate reading
        print(f"[Reader] Read value: {shared_data}")
        time.sleep(random.uniform(0.01, 0.1))

def writer():
    global shared_data
    for i in range(10):
        # Simulate writing
        shared_data += 1
        print(f"[Writer] Wrote value: {shared_data}")
        time.sleep(random.uniform(0.01, 0.1))

def run_without_lock():
    print("=== Running WITHOUT lock (expect messy output) ===")
    t1 = threading.Thread(target=reader)
    t2 = threading.Thread(target=writer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def run_with_lock():
    print("\n=== Running WITH lock (output should be clean) ===")
    lock = threading.Lock()
    
    def reader_locked():
        global shared_data
        for _ in range(10):
            with lock:
                print(f"[Reader] Read value: {shared_data}")
            time.sleep(random.uniform(0.01, 0.1))

    def writer_locked():
        global shared_data
        for i in range(10):
            with lock:
                shared_data += 1
                print(f"[Writer] Wrote value: {shared_data}")
            time.sleep(random.uniform(0.01, 0.1))

    t1 = threading.Thread(target=reader_locked)
    t2 = threading.Thread(target=writer_locked)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    run_without_lock()
    # Reset shared_data for the next run
    shared_data = -1
    run_with_lock()