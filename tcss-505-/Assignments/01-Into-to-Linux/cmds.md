# Commands

## Question 1 – How many total processes are present shortly after the Ubuntu VM boots up?

ps -e | wc -l

## Question 2 – How many total threads are present shortly after the Ubuntu VM boots up?

ps -eLf | wc -l

## Question 3 – What is the version number of the Linux kernel installed on your Ubuntu VM?

uname -r

## Question 4 – What is the model name of the CPU(s) of the VM?

lscpu | grep "Model name"

## Question 5 – What is the total size of the memory swap space (virtual memory) in MB on the VM?

free -m | grep "Swap" | awk '{print $2}'

## Question 6 – What is the free disk space of the root disk partition in MB?

df -m / | tail -1 | awk '{print $4}'

## Question 7 – What is the total number of inodes on the root filesystem?

df -i / | tail -1 | awk '{print $2}'

## Question 8 – What is the average round trip time (RTT) of 10 ICMP ping packets from your Ubuntu VM to <www.google.com>?

ping -c 10 <www.google.com> | tail -1 | awk -F '/' '{print $5}'
