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

A4. SJF delivers the same turnaround times as FIFO in two specific scenarios:

1. When all jobs have the same length:
   - As demonstrated in Q1, when all jobs are identical in length (e.g., all 200 time units)
   - In this case, SJF has no advantage in reordering since all jobs take the same time
   - The order of execution doesn't affect the total turnaround time

2. When jobs arrive in order of increasing length:
   - As demonstrated in Q2, when jobs arrive in ascending order of their lengths (e.g., 100, 200, 300)
   - In this case, FIFO's natural order matches SJF's optimal order
   - No reordering is needed to achieve the best possible turnaround time

In all other cases, particularly when longer jobs arrive before shorter ones, SJF will typically produce better average turnaround times than FIFO by reordering the jobs to run the shortest ones first.

Q6. What happens to response time with SJF as job lengths increase?
Can you use the simulator to demonstrate the trend?

A6. With SJF scheduling, as job lengths increase, the response time for longer jobs tends to increase significantly. This is because:

1. Shortest Job First Principle:
   - SJF always prioritizes the shortest available job
   - When a long job arrives, it must wait for all shorter jobs to complete
   - As more short jobs arrive, the long job's wait time (response time) increases

2. Response Time Impact:
   - Short jobs maintain good response times as they are prioritized
   - Long jobs experience increasingly poor response times
   - The average response time can become very high if there are many short jobs arriving before long jobs

3. Example Scenario:
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

Q2. How would you run the scheduler to reproduce each of the exam-
ples in the chapter?

Q3. How would you configure the scheduler parameters to behave just
like a round-robin scheduler?

Q4. Craft a workload with two jobs and scheduler parameters so that
one job takes advantage of the older Rules 4a and 4b (turned on
with the -S flag) to game the scheduler and obtain 99% of the CPU
over a particular time interval.

Q5. Given a system with a quantum length of 10 ms in its highest queue,
how often would you have to boost jobs back to the highest priority
level (with the -B flag) in order to guarantee that a single long-
running (and potentially-starving) job gets at least 5% of the CPU?