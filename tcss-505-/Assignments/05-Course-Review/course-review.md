# Course Review

## What is your favorite thing about TCSS 505?

I loved learning about the nuances between operating systems. I have always primarily used windows for development and Linux for servers, but it made me really want to try Linux as a daily driver just seeing how easy it is to get around things and get things running.
I also enjoyed seeing how virtualization works on a lower level and how it can be used. I don’t have much experience at the lower level of using containers and gaining a view on them was enlightening.

## What are the three main forms of virtualization in operating systems, what are the virtual forms of the CPU, Memory, and Disk?

 Virtualization Virtual Form Explanation:
CPU Virtualization
 Process The operating system creates the illusion that each running program (process) has its own dedicated CPU. This is achieved through time-sharing, where the OS rapidly switches between processes using context switching, giving the appearance of parallelism.
Memory Virtualization
 Virtual Address Space  Each process is given the illusion that it has access to a large, contiguous block of memory starting at address zero. This is implemented using paging and segmentation, allowing processes to operate independently and securely without interfering with each other’s memory
Disk Virtualization
 File Instead of dealing with raw disk blocks, users and applications interact with files. The file system abstracts the physical storage into a logical hierarchy of files and directories, managing access, storage, and metadata.

## What are the three major components of a process in memory? Describe how they are laid out (organized). Include in your description how free memory is managed

- Stack
  - This is the highest level of memory. It’s used for function calls, local variables, and control flow. It grows downward.
  - Free memory is the space between the heap and the stack. The OS and memory allocator manages this space to prevent memory collision between the two.

- Heap
  - This is a dynamically allocated memory that grows upward. It stores memory used by a program at runtime.

- Code
  - This contains the executable instructions of the program. It is typically read-only to prevent accidental modification. Shared among processes running the same program to save memory.
  - Stack
  - Free Memory
  - Heap
  - Code

## Describe the process of translating the virtual address system used by a process to physical addresses. Include in your discussion how the OS uses base and bound to ensure memory access remains within the assigned address space

When a process assesses memory, the “bounds” are checked and the address is translated. The hardware checks if the virtual address is less than the assigned bound and raises an exception if it is not. If it is valid, the hardware adds the base to the virtual address to find the physical address” physical address = virtual address + base). This ensures that each process can only access memory within its own allocated region.
The operating system sets the bound registries when the process is scheduled, ensuring isolation between the memory of processes and manages free memory to prevent collisions.

## Describe the steps the OS goes through to swap out a process and load another so the second process can be executed, what is this swapping process called?

This is called context switching and can be a costly process. First the OS determines the process to be swapped out. Second, the OS saves the processes “context” and memory. Third, the OS marks the process’s page as not present in memory. Fourth, physical memory is marked as free and available for other processes. Fifth, the new process is selected and loaded into memory. Sixth, the OS restores the context and memory of the new process and finally the process is executed.

## Describe a Multi-Level Feedback Queue. What does the priority boost prevent?

MLFQ is a process scheduling algorithm that uses multiple queues with different priorities to dynamically adjust a processes priority based on its behavior including task pauses and long running jobs. Priority boost prevents long running tasks from getting stuck in low priority queues and not being allowed to finish execution.

## Describe the basics of Stride Scheduling. How does Stride Scheduling differ from Lottery Scheduling?

Stride scheduling is a process scheduling that ensures each process gets proportional CPU time based on assigned shares. Each process gets a certain number of shares. The stride is then calculated based on the number of tickets assigned to a process. Each process maintains a pass value initially set to 0. The schedular always picks the lowest pass value that is then incremented by the stride. It is a deterministic schedular that ensures that all processes get process time based around the number of shares.
The Lottery schedular has the OS randomly picking processes based on the tickets assigned to the process. It is a probabilistic scheduling algorithm.

## Describe paging and how it helps the OS manage memory for processes

Paging divides virtual and physical memory into fixed sized blocks of Pages for virtual memory and Frames for physical memory. Each process has its own page table that maps these pages and frames. It allows the OS to isolate processes by assigning them non-overlapping frames and gives the OS more flexibility in how is assigned memory to these processes.

## What is a Translation Lookaside Buffer? How can hits be improved? (HINT: think about spatial locality and how to increase it)

A Translation Lookaside Buffer is a small, fast hardware cache used to speed up virtual/physical address translation in systems that use paging. When hardware is looking for a physical address from a virtual address the cache is used to find recently used translations more quickly. The rate at which this cache is hit without results can be reduced can be reduced by increasing page sizes to allow the TLB to cover more memory or by grouping related data physically close together.

## What is a thread? How does it differ from a process? How can information be passed between multiple threads or multiple processes? How does that differ?

A thread is the basic unit of CPU utilization. It’s a light process which shares memory with its peers. Multiple threads share memory, code section, a heap, and other resources including  open files. A process on the other hand, has its own dedicated memory and must communicate with other processes through an IPC protocol such as pipes and queues. This is slower than a thread which shares memory but requires synchronization to avoid race conditions.

## Describe the basic mechanics of the lock process. What do locks prevent?

A lock is a mechanism to prevent multiple threads from accessing a subset of code which accesses shared memory to prevent race conditions where a shared resource being used by these threads can cause bugs or exceptions in your code. It works by requiring the “lock” for access to the block of code. If the lock is available the threads can access the code, otherwise it must wait until the lock is available. Once the thread has executed the required code it releases the lock for other threads.

## What does a Canonical IO Device provide for the OS to communicate with it, issue commands, and provide data access?

A Canonical IO device is an abstraction that provides a standard interface for interactions between the OS and the hardware devices on the system. It provides a set of registries for communication and a standardized protocol for interacting with the devices. This is a defined sequence of steps for these interactions. It also typically provides an interrupt mechanism so the OS in not blocked from other processes.

## Describe an inode

An inode contains the metadata for a file including the file type, file size, ownership permissions, timestamp, etc. It’s created by the OS when the file is created to find files in the 
directory and allows the OS to manage the file.

## Describe the principles behind Direct Execution and it's advantages/disadvantages compared to Limited Direct Execution

Direct execution allows a user to directly run a process on the CPU without interacting with the OS. This can be nice as it can run much faster without worrying about the OS slowing down the process but loses the protections the OS provides including data security/protection and enforcing scheduling.
Limited Direct Execution is a nice middle ground that allows the OS to run in kernel mode with direct access to the CPU. Privileged access calls still run through the OS in kernel mode, and then control is given back to the user. This is the standard mode of running applications on an OS.

## Describe 2 advantages of utilizing virtual machines and the Linux operating system

VM’s

1. Strong isolation, allowing one VM to crash without crashing the entire system
2. Resource efficiency where multiple VM’s can share resources through virtualization and scheduling

Linux

1. Strong community of power users means that new features are readily available and fixes/work arounds can be could quickly and typically for free.
2. Light weight OS can run on older systems much faster than resource intensive Windows.
