#!/bin/bash

# Make the Python script executable
chmod +x a1_armstrong.py

# Create a results file
echo "Processes,Runtime (ms)" > benchmark_results.csv

# Run the program with 1 to 10 processes
for i in {1..10}
do
    echo "Running with $i process(es)..."
    # Run the program and capture the runtime from the last line
    runtime=$(./a1_armstrong.py -n 1000000 -p $i | grep "Runtime" | awk '{print $2}')
    # Append results to CSV
    echo "$i,$runtime" >> benchmark_results.csv
done

echo "Benchmark complete! Results saved in benchmark_results.csv" 