#!/bin/bash

# Make the Python script executable
chmod +x a1_armstrong.py

# Run the program with 1 to 10 processes
for i in {1..10}
do
    echo "Running with $i process(es)..."
    # Run the program and capture the runtime from the last line
    runtime=$(./a1_armstrong.py -n 1000000 -p $i | grep "It took" | awk '{print $3}')
    # Append results to CSV
    echo "$i,$runtime"
done

echo "Benchmark complete! Results saved in benchmark_results.csv" 
