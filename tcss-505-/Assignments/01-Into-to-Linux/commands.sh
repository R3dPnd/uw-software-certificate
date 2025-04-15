#!/bin/bash

# Question 1 – How many total processes are present shortly after the Ubuntu VM boots up?
echo "Total processes:"
echo "# --------------------------------------------------------------------"
ps -e | wc -l

# Question 2 – How many total threads are present shortly after the Ubuntu VM boots up?
echo "Total threads:" 
echo "# --------------------------------------------------------------------"
ps -eLf | wc -l

# Question 3 – What is the version number of the Linux kernel installed on your Ubuntu VM?
echo "Linux kernel version:" 
echo "# --------------------------------------------------------------------"
uname -r

# Question 4 – What is the model name of the CPU(s) of the VM?
echo "CPU model name:" 
echo "# --------------------------------------------------------------------"
lscpu | grep "Model name"

# Question 5 – What is the total size of the memory swap space (virtual memory) in MB on the VM?
echo "Total swap memory (MB):" 
echo "# --------------------------------------------------------------------"
free -m | grep "Swap" | awk '{print $2}'

# Question 6 – What is the free disk space of the root disk partition in MB?
echo "Free disk space on root partition (MB):" 
echo "# --------------------------------------------------------------------"
df -m / | tail -1 | awk '{print $4}'

# Question 7 – What is the total number of inodes on the root filesystem?
echo "Total inodes on root filesystem:" 
echo "# --------------------------------------------------------------------"
df -i / | tail -1 | awk '{print $2}'

# Question 8 – What is the average round trip time (RTT) of 10 ICMP ping packets from your Ubuntu VM to www.google.com?
echo "Average RTT to www.google.com (ms):" 
echo "# --------------------------------------------------------------------"
ping -c 10 www.google.com | tail -1 | awk -F '/' '{print $5}'