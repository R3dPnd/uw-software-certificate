#!/bin/bash

# Question 1 – How many total processes are present shortly after the Ubuntu VM boots up?
echo "Total processes:"
echo "# --------------------------------------------------------------------"
echo "ps -e | wc -l"
ps -e | wc -l

# Question 2 – How many total threads are present shortly after the Ubuntu VM boots up?
printf "\nTotal threads:" 
echo "# --------------------------------------------------------------------"
echo "ps -eLf | wc -l"
ps -eLf | wc -l

# Question 3 – What is the version number of the Linux kernel installed on your Ubuntu VM?
printf "\nLinux kernel version:" 
echo "# --------------------------------------------------------------------"
echo "uname -r"
uname -r

# Question 4 – What is the model name of the CPU(s) of the VM?
printf "\nCPU model name:" 
echo "# --------------------------------------------------------------------"
echo "lscpu | grep "Model name""
lscpu | grep "Model name"

# Question 5 – What is the total size of the memory swap space (virtual memory) in MB on the VM?
printf "\nTotal swap memory (MB):" 
echo "# --------------------------------------------------------------------"
echo "free -m | grep "Swap" | awk '{print $2}'"
free -m | grep "Swap" | awk '{print $2}'

# Question 6 – What is the free disk space of the root disk partition in MB?
printf "\nFree disk space on root partition (MB):" 
echo "# --------------------------------------------------------------------"
echo "df -m / | tail -1 | awk '{print $4}'"
df -m / | tail -1 | awk '{print $4}'

# Question 7 – What is the total number of inodes on the root filesystem?
printf "\nTotal nodes on root filesystem:" 
echo "# --------------------------------------------------------------------"
echo "df -i / | tail -1 | awk '{print $2}'"
df -i / | tail -1 | awk '{print $2}'

# Question 8 – What is the average round trip time (RTT) of 10 ICMP ping packets from your Ubuntu VM to www.google.com?
printf "\nAverage RTT to www.google.com (ms):" 
echo "# --------------------------------------------------------------------"
echo "ping -c 10 www.google.com | tail -1 | awk -F '/' '{print $5}'"
ping -c 10 www.google.com | tail -1 | awk -F '/' '{print $5}'