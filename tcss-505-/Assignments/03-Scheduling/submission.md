# Assignemnt 3: Scheduler

## Chapter 7

Q1. Compute the response time and turnaround time when running
three jobs of length 200 with the SJF and FIFO schedulers.

A1.

| Job         | FIFO Response Time | FIFO Turnaround Time | SJF Response Time | SJF Turnaround Time |
|-------------|-------------------|-----------------------|-------------------|---------------------|
| Job 1 (200) |         0         |       200             |         0         |         200         |
| Job 2 (200) |         200       |       400             |         200       |         400         |
| Job 3 (200) |         400       |       600             |         400       |         600         |
| **Average** |        **200**    |       **400**         |         **200**   |         **400**     |

Note: Since all jobs have the same length (200), SJF and FIFO produce identical results. This is because SJF's advantage of prioritizing shorter jobs doesn't come into play when all jobs are the same length.

Q2. Now do the same but with jobs of different lengths: 100, 200, and
300.

A2.

| Job         | FIFO Response Time | FIFO Turnaround Time | SJF Response Time | SJF Turnaround Time |
|-------------|-------------------|-----------------------|-------------------|---------------------|
| Job 1 (100) |         0         |         100           |         0         |         100         |
| Job 2 (200) |         100       |         300           |         100       |         300         |
| Job 3 (300) |         300       |         600           |         300       |         600         |
| **Average** |        **133.33** |       **333.33**      |       **133.33**  |       **333.33**    |

Note: In this case, both schedulers produce the same results because the jobs arrive in order of increasing length (100, 200, 300). If the jobs had arrived in a different order, SJF would have reordered them to run the shortest job first, potentially improving the average turnaround time.

Q4. For what types of workloads does SJF deliver the same turnaround
times as FIFO?

A4. SJF delivers the same turnaround times as FIFO in two specific scenarios when all jobs have the same length or when jobs arrive in order of increasing length as demnstrated by Q1.

In all other cases, particularly when longer jobs arrive before shorter ones, SJF will typically produce better average turnaround times than FIFO by reordering the jobs to run the shortest ones first.

Q6. What happens to response time with SJF as job lengths increase?
Can you use the simulator to demonstrate the trend?

A6. With SJF scheduling, as job lengths increase, the response time for longer jobs tends to increase significantly. This is because the longer jobs h]are not priorite\zed by the SJF scheular and have to wait for the shortest jobs to finish.

Example Scenario:
   Consider these jobs arriving at time 0:

- Job A: 500 time units
- Job B: 100 time units
- Job C: 50 time units
- Job D: 200 time units

   The response times would be:
- Job C (50): 0 (starts immediately as shortest)
- Job B (100): 50 (starts after Job C)
- Job D (200): 150 (starts after Job B)
- Job A (500): 350 (starts last as longest)

This demonstrates how the longest job (A) must wait for all shorter jobs to complete, leading to a poor response time of 350.

This behavior makes SJF less suitable for interactive systems where response time is critical, as long jobs might experience unacceptable delays.

## Chapter 8

Q1. Run a few randomly-generated problems with just two jobs and
two queues; compute the MLFQ execution trace for each. Make
your life easier by limiting the length of each job and turning off
I/Os.

A1. I ran two MLFQ simulations with two jobs and two queues, with I/O disabled. Here are the results:

Simulation 1 (seed=1): mlfq.py -j 2 -n 2 -M 0 -m 50 -s 1 -c

- Job 0: startTime 0, runTime 7, ioFreq 0
- Job 1: startTime 0, runTime 38, ioFreq 0
- Configuration: 2 queues, quantum=10 for both queues, allotment=1 for both queues
- Execution Trace:
  - Both jobs start at time 0
  - Job 0 runs first at priority 1 (highest) and completes at time 7
  - Job 1 runs at priority 1 until time 16, then drops to priority 0
  - Job 1 completes at time 45
- Statistics:
  - Job 0: response time = 0, turnaround time = 7
  - Job 1: response time = 7, turnaround time = 45
  - Average: response time = 3.50, turnaround time = 26.00

Simulation 2 (seed=2): mlfq.py -j 2 -n 2 -M 0 -m 50 -s 2 -c

- Job 0: startTime 0, runTime 47, ioFreq 0
- Job 1: startTime 0, runTime 3, ioFreq 0
- Configuration: 2 queues, quantum=10 for both queues, allotment=1 for both queues
- Execution Trace:
  - Both jobs start at time 0
  - Job 0 runs first at priority 1 until time 9
  - Job 1 runs at priority 1 from time 10-12 and completes
  - Job 0 continues at priority 0 until completion at time 50
- Statistics:
  - Job 0: response time = 0, turnaround time = 50
  - Job 1: response time = 10, turnaround time = 13
  - Average: response time = 5.00, turnaround time = 31.50

Q2. How would you run the scheduler to reproduce each of the examples in the chapter?

A2. To reproduce the three examples from Chapter 8, we can use the following MLFQ simulator configurations:

Example 1 (Single Long-Running Job):

```bash
python mlfq.py -n 3 -j 1 -l 0,200,0 -c
```

This creates:

- 3 queues (Q0, Q1, Q2)
- 1 job that runs for 200 time units
- Job starts at time 0
- No I/O (ioFreq=0)
- Will show the job moving from Q2 to Q1 to Q0

Example 2 (Long Job + Short Job):

```bash
python mlfq.py -n 3 -j 2 -l 0,200,0:100,20,0 -c
```

This creates:

- 3 queues
- 2 jobs:
  - Job 0: starts at 0, runs for 200 units
  - Job 1: starts at 100, runs for 20 units
- Shows how the short job gets priority when it arrives

Example 3 (I/O-intensive Job):

```bash
python mlfq.py -n 3 -j 2 -l 0,200,0:0,1,1 -c
```

This creates:

- 3 queues
- 2 jobs:
  - Job 0: long-running CPU job (200 units)
  - Job 1: interactive job (1 unit CPU, then I/O)
- Demonstrates how I/O jobs maintain high priority

Q3. How would you configure the scheduler parameters to behave just
like a round-robin scheduler?

A3. To make MLFQ behave like a round-robin scheduler, we need to configure it to eliminate priority-based scheduling. Here's how:

```bash
python mlfq.py -n 1 -q 10 -B 0 -M 0 -c
```

Key parameters:

- -n 1: Use only one queue (eliminates priority levels)
- -q 10: Set quantum length to 10 time units (or any desired value)
- -B 0: Disable priority boosting
- -M 0: Disable I/O (since round-robin doesn't handle I/O specially)

This configuration works because:

1. Single queue (-n 1) means all jobs have the same priority
2. Fixed quantum (-q 10) ensures each job gets equal time slices
3. No priority changes (-B 0) means jobs stay in the same queue
4. No I/O (-M 0) simplifies the scheduling to pure time-slicing

When run with these parameters, MLFQ will:

- Treat all jobs equally
- Give each job a fixed time slice
- Cycle through jobs in order
- Not consider job length or I/O behavior

This is equivalent to basic round-robin scheduling where:

- Jobs run in a circular order
- Each job gets the same amount of CPU time
- No job gets priority over others
- Scheduling is fair but may not be optimal for turnaround time

Q4. Craft a workload with two jobs and scheduler parameters so that
one job takes advantage of the older Rules 4a and 4b (turned on
with the -S flag) to game the scheduler and obtain 99% of the CPU
over a particular time interval.

A4. To demonstrate how a job can game the MLFQ scheduler using the older rules, we can create a workload where one job issues I/O requests just before its time slice expires. Here's the configuration:

```bash
python mlfq.py -n 3 -j 2 -l 0,200,0:0,200,9 -S -c
```

This configuration:

- Uses 3 queues (-n 3)
- Has 2 jobs:
  - Job 0: A normal long-running job (200 time units, no I/O)
  - Job 1: A gaming job that issues I/O every 9 time units
- Enables the -S flag to use older rules where jobs maintain priority after I/O

How the gaming works:

1. Job 1 starts at highest priority (Q2)
2. It runs for 9 time units (just before its 10-unit quantum expires)
3. It issues an I/O request
4. Due to -S flag, it maintains its high priority when it returns from I/O
5. This cycle repeats, keeping Job 1 at high priority
6. Job 0 eventually drops to lower priority queues

The key to gaming the system:

- The gaming job (Job 1) issues I/O just before its quantum expires
- With -S flag, it never drops in priority
- It effectively stays in the highest priority queue
- The other job (Job 0) will drop to lower priorities
- This results in Job 1 getting most of the CPU time

Q5. Given a system with a quantum length of 10 ms in its highest queue,
how often would you have to boost jobs back to the highest priority
level (with the -B flag) in order to guarantee that a single long-
running (and potentially-starving) job gets at least 5% of the CPU?

A5. To guarantee a long-running job gets at least 5% of the CPU, we need to calculate how often to boost jobs back to the highest priority. Let's solve this step by step:

1. Given:
   - Quantum length = 10 ms in highest queue
   - Target CPU share = 5% (0.05)
   - Need to find boost interval (-B value)

2. Analysis:
   - When a job is boosted, it gets one quantum (10 ms) at highest priority
   - To get 5% CPU share, the job needs 5% of the time between boosts
   - If we boost every B ms, the job needs 0.05 × B ms of CPU time
   - Each boost gives 10 ms of CPU time
   - Therefore: 10 ms = 0.05 × B

3. Calculation:

10 ms = 0.05 x B
B = 10ms/0.05
B = 200

Therefore, we need to set -B 200 to guarantee the long-running job gets at least 5% of the CPU.

This can be verified with the following configuration:

```bash
python mlfq.py -n 3 -j 2 -l 0,200,0:0,200,0 -B 200 -c
```
