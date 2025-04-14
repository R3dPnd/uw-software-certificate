# Intro to Linux

The purpose of this assignment is to create a local Linux Virtual Machine for use in future projects and to gain experience using Ubuntu. Please download and install Ubuntu 24.04. During the installation, a “normal installation” is recommended.

## Task 1 – Install your Virtual Machine Software (Hypervisor)

Windows and Intel Macs:

Oracle VirtualBox can be downloaded from: <https://www.virtualbox.org/wiki/DownloadsLinks> to an external site.

 Assuming you have access to a computer, choose the appropriate link from the list for your host operating system to download VirtualBox: Version 6.1.x is now available:

Windows hosts

OS X (macOS) hosts. If you have trouble with Virtual Box on MacOS try downloading UTM.

If you do not have access to a computer for Virtual Box and Ubuntu, Stephen Rondeau, senior computer specialist for the School of Engineering and Technology, will create Ubuntu 24.04 based VirtualBox VMs. If you haven’t already requested a VM to be setup using the VM-survey, please contact the instructor by email or by sending a message via Canvas.

Apple Silicon Macs:

I recommend downloading UTM: <https://mac.getutm.app/Links> to an external site.

Other Options:

I personally use Parallels as my virtual machine software. It's not free but provides a very smooth experience: <https://www.parallels.com/ca/products/desktopLinks> to an external site.

VMWare Fusion/Workstation Pro are another premium option:

Fusion: <https://www.vmware.com/content/vmware/vmware-published-sites/us/products/fusion.html.htmlLinks> to an external site.

Workstation Pro: <https://www.vmware.com/products/workstation-pro.htmlLinks> to an external site.

## Task 2 – Create a Ubuntu 24.04 LTS VM

The Ubuntu 22.04 disk image (ISO) can be downloaded from: <https://ubuntu.com/download/desktopLinks> to an external site.

The recommended configuration for your virtual machine is 4GB+ RAM (2GB minimum, more if available), 2 or more CPU cores, and a minimum of 20 GB free disk space. 20-40+ GB is recommended if planning to use the Ubuntu VM after the class. Previously, students with 10GB or less VMs have run out of disk space near the end of the quarter leading to headaches. I also recommend maxing out the available VRAM setting to have a smoother experience.

Virtual Box Installation:

Video on 64-bit Ubuntu Installation (Windows 10):

<https://youtu.be/x3Zpe1rIPFELinks> to an external site.

Video on 64-bit Ubuntu Installation (MacOS):

<https://youtu.be/Hzji7w882OYLinks> to an external site.

After installing Ubuntu, install the Linux Guest Additions:

<https://youtu.be/Kbez-XdXqrwLinks> to an external site.

"Guest Additions" enable sharing of the Host OS Hard Disk (e.g. Windows, Mac) with the Virtual Machine. Guest Additions also enable sharing of the clipboard, and provide mouse pointer integration. Please spend the additional time to install the Guest Additions. You’ll be happy that you did!

Once your VM has been installed, select the VM under Virtual Box, and select “Settings”. Under “General”, go to the “Advanced” tab, and enable the “Bidirectional” clipboard. This will allow you to copy-and-paste between your host (laptop) and guest (VM). Also, on the left-hand-side, select “Shared Folders”. Add a new shared folder by clicking on the folder icon with a green-plus sign on the right. One or more folders from your host (laptop) can be shared with the guest (VM). Shared folders often will then appear under “/media” on the Ubuntu filesystem. These file system mounts can be viewed using the ”df -h” Linux command. Note: you may need “superuser” permissions to access these file system mounts. To become superuser type “sudo bash” and then “cd /media/{dir-name}”. Take note that modifications as super user will use the “root” user and not your typical user account. Review Linux file permissions including the commands chmod, chown, and chgrp to learn how to change permissions. “mv” and “cp” can move and copy files from /media to other locations.

Apple Silicon UTM Installation:

Create an Ubuntu 22.04 (ARM64) VM using the UTM Gallery: <https://mac.getutm.app/galleryLinks> to an external site.

## Task 3 – Become familiar with Linux

For this task, use the internet, and/or a good Linux book to discover Linux commands that provide answers to each of the questions. The commands will help describe information about your Ubuntu Virtual Machine. The goal is to become familiar with common Linux commands and to provide an opportunity to gain experience using the internet and various references to discover how to navigate and introspect information about Linux.

50% of the credit is for determining a command to display the answer. The other 50% is for interpreting the output of the command to answer the question.

Discover a Linux command (sequence) that provides an answer to each question. Each question potentially has many valid Linux commands that could answer the question. You’re only responsible for finding one possible command. Any command, or sequence of commands, is OK as long as the correct answer is obtained.

Note #1: manually printing out the answer using the “echo” statement, is not sufficient. Answers must be from using Linux system commands.

Note #2: It is not necessary to parse the value from the command(s) to provide an EXACT answer. Reporting the full output of a command that contains the correct answer is OKAY!

Terminal Controls Cheat-Sheet:

Up/Down Arrows: Navigate command history.

Tab: Autocomplete

Enter: Run command

Ctrl-C: Close program (may be overridden by running program)

cd: Change directory (TIP: cd .. will go back 1 folder)

ls: List directly contents (TIP: ls /bin will show all programs installed)

man: Open manual for command, use up/down arrows to scroll, hit q to quit.

# !:  A shebang, will be put at the beginning of a text file to tell the terminal what program to run the file with. For example bash programs will start with #!/bin/bash

sudo ___: Superuser Do, allows you to run programs with additional permissions. Similar to running a program "As Administrator" on Windows.

sudo apt install ___: Installs a program. For this class I recommend installing the following programs:

sudo apt install micro neofetch fish htop build-essential jq curl

TIP: Check out the manual page for some of these programs to know what they do (they may be helpful for the next section).

## Questions

### Question 1 – How many total processes are present shortly after the Ubuntu VM boots up?

Note: specify a non-interactive command to answer the question.

### Question 2 – How many total threads are present shortly after the Ubuntu VM boots up? Note: specify a non-interactive command to answer the question.

### Question 3 – What is the version number of the Linux kernel installed on your Ubuntu VM?

### Question 4 – What is the model name of the CPU(s) of the VM? According to wikipedia or Intel/AMD specification pages, how many CPU cores does this CPU have? If the information is available, what was the release date of the CPU, and the original retail price?

### Question 5 – What is the total size of the memory swap space (virtual memory) in MB on the VM?

### Question 6 – What is the free disk space of the root disk partition in MB? In Linux, the root partition is always mounted at “/”. A mount point is the directory or location in the file system where an I/O device has been mounted. The mount point is used to access the device through a file system.

### Question 7 – What is the total number of inodes on the root filesystem? If unfamiliar with what an inode is, look up the definition and how to display the number of free/used inodes on Linux/Ubuntu.

### Question 8 – What is the average round trip time (RTT) of 10 ICMP ping packets from your Ubuntu VM to <www.google.com>?

### Question 9 - What is the interface name of the network interface device used to route the ICMP ping packets to <www.google.com>?

### Question 10 – Identify the file system type of the “/” root partition?

Briefly describe this file system type (1-2 sentences).
Using the Linux manual pages, look up the file system type. The manual pages identify the Linux kernel version when specific features were added to the file system. List the name of two features added to the filesystem since July 2017. Search the manual page and include a description for one of these features. The descriptions should appear in the manual page.

### BONUS 1 (2 points) Look up 2 Linux commands you are unfamiliar with (find all programs by doing ls /usr/bin and read their manual page with man). Provide an example of using the command in your script. In the textfile that contains the answers to the questions, provide a description in your own words of what the command does and an example of when it might be useful.

### BONUS 2 (2 points) Write a short review (~300 words) about the Ubuntu operating system. What do you think of the UI, installed programs, etc? How does it compare to the OS you're used to? Try installing new programs. How was the overall experience? Then create another VM with a different Linux distribution. Some options include Linux Mint, PopOS, Manjaro, Debian, Fedora, Zorin, CentOS, etc. Write one more short review of that operating system and compare it to Ubuntu. Obvious AI answers that simply regurgitate information on the distribution's website in a bulleted list will not be accepted.

## What to Submit

### File #1: BASH SCRIPT (a0.sh file)

For the assignment, submit a BASH script that contains the list of commands to answer each of the questions.

How to create a simple bash script:

Create a “bash” script which provides the commands to answer each of the questions. Include separator lines and comments for each command. Also include “echo” statements to label command sequences on the output, and provide spacing “breaks” between commands.

Use an editor such as "micro" or “nano” to create a script, “a0.sh”:

Sample Script:

Question #1: What is the command to show the user’s current working directory?

## Question #1

echo ; echo “command #1: pwd”
pwd

## Question #2

...

To run the script assign the script to have execute permission Give the “user” (u) “execute” (x) permission with chmod (u+x): $ chmod u+x a0.sh

File #2: ANSWERS FILE (a0_answers.txt file)

Create a text file called “a0_answers.txt”.
Include the output from each command in a0.sh and interpret the output to answer each of the questions. Write a short explanation of what the command(s) you are using is, what the flags do, and what in the output is the answer to the question. For example, Ping will likely output many numbers and you need to explain which is the round trip time.

$ micro a0_answers.txt
[Add text to answer each question]

1. Output:

System info --- Processes: 150 --- Threads: 12

Explanation:

To answer this I used the "this_is_a_fake_answer" program with the "-P" flag to list information about process and threads. Shortly after boot there was 150 Processes.

2. (q2 answer)
...
[Save the file, Exit Micro.]

For this assignment, you will then submit two files to Canvas:

“a0.sh” Bash Script contains a list of commands to answer each of the questions.
“a0_answers.txt” File provides your interpretation of the answers to each of the questions.

Grading

This assignment will be scored out of 20 points. (20/20)=100%

Each question is worth 2 points: one point is for answering the question correctly in a0_answers.txt, and one point is for including a valid command in a0.sh. Answering the bonus questions will be worth up to 4 extra points.

Please create, format, and submit two text files to Canvas with the specified names to submit the assignment. Failure to provide the two files will result in the loss of 3 points:

File #1: a0.sh

File #2: a0_answers.txt
