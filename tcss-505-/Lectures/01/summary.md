# Summary

## Key Points

### Virtual Machines (VMs)

* VMs allow you to run multiple operating systems on a single machine.
* Tools like VirtualBox (Windows/Intel Mac) and UTM (Apple Silicon Mac) are used to create VMs.
* VMs provide isolation, snapshots, and portability.

### Operating System (OS) Concepts

* OS vitalizes hardware resources like CPU, memory, and storage.
* Virtual forms:
* CPU → Processes and Threads.
* Memory → Virtual Address Space.
* Storage → File System.
* OS manages resources, provides abstraction, and ensures security and reliability.

### Processes and Threads

* Processes are independent programs running on the OS.
* Each process has its own memory space.
* Multiple processes can run concurrently.

### Memory Virtualization

Each process has its own virtual address space.
The OS maps virtual memory to physical memory.

### File System

Provides persistent storage for data.
OS handles file operations like reading, writing, and managing storage devices.

### Linux Terminal Basics

Terminal commands are powerful for navigating and managing files.
Commands like cd, ls, cp, mv, and rm are essential.

### Assignment 1

Create and configure a VM.
Practice Linux commands to navigate and manipulate files.

## Next Steps

1. Set Up a Virtual Machine

    * Download and install VirtualBox (Windows/Intel Mac) or UTM (Apple Silicon Mac).
    * Create a VM and install Ubuntu 22.04 LTS.

2. Practice Linux Commands

    * Navigate directories, create files, and manage processes using terminal commands.

3. Complete Assignment 1:

    * Follow the instructions to explore Linux commands and answer the provided questions.
    * Prepare for Next Lecture:

4. Review concepts of concurrency and CPU virtualization.

## Linux Commands Mentioned

### Navigation

* cd [directory] - Change directory.
* cd .. - Move up one directory.
* ls - List directory contents.
* ls -l - List directory contents in long format.

### File Management

* mkdir [directory_name] - Create a new directory.
* mv [source] [destination] - Move or rename a file.
* cp [source] [destination] - Copy a file.
* rm [file_name] - Remove a file.

### Process Management

* Ctrl+C - Stop a running program.
* Ctrl+Z - Pause a running program.
* fg - Bring a paused program to the foreground.

### Other Commands

* man [command] - Open the manual for a command.
* gcc -o [output_file] [source_file] - Compile a C program.
* ./[executable] - Run an executable file.
