#!/bin/bash

# Question 1 – How many total processes are present shortly after the Ubuntu VM boots up?
echo "Question 1 – How many total processes are present shortly after the Ubuntu VM boots up?"
echo "# --------------------------------------------------------------------"
echo "ps -e | wc -l"
ps -e | wc -l
echo the ps command lists out the running processes, 
echo "-e option lists all processes, "
echo "and wc -l counts the number of lines in the output."

# Question 2 – How many total threads are present shortly after the Ubuntu VM boots up?
printf "\nQuestion 2 – How many total threads are present shortly after the Ubuntu VM boots up?" 
echo "# --------------------------------------------------------------------"
echo "ps -eLf | wc -l"
ps -eLf | wc -l
echo the ps command lists out the running processes,
echo "-e option lists all processes, "
echo "-L option lists all threads, "
echo "and wc -l counts the number of lines in the output."
echo "The output of the ps command is piped to wc -l to count the number of lines, which gives the total number of threads."

# Question 3 – What is the version number of the Linux kernel installed on your Ubuntu VM?
printf "\nQuestion 3 – What is the version number of the Linux kernel installed on your Ubuntu VM?" 
echo "# --------------------------------------------------------------------"
echo "uname -r"
uname -r
echo the uname command prints system information,
echo "-r option prints the kernel version number."
echo "The output of the uname command is the version number of the Linux kernel installed on the system."

# Question 4 – What is the model name of the CPU(s) of the VM?
printf "\nQuestion 4 – What is the model name of the CPU(s) of the VM?" 
echo "# --------------------------------------------------------------------"
echo "lscpu | grep "Model name""
lscpu | grep "Model name"
echo the lscpu command prints CPU architecture information,
echo "and grep "Model name" filters the output to show only the model name of the CPU(s)."
echo "The output of the lscpu command is the model name of the CPU(s) installed on the system."

# Question 5 – What is the total size of the memory swap space (virtual memory) in MB on the VM?
printf "\nQuestion 5 – What is the total size of the memory swap space (virtual memory) in MB on the VM?" 
echo "# --------------------------------------------------------------------"
echo "free -m | grep "Swap" | awk '{print $2}'"
free -m | grep "Swap" | awk '{print $2}'
echo the free command displays memory usage information,
echo "-m option displays the information in MB, "
echo "and grep "Swap" filters the output to show only the swap space information."
echo "The awk command is used to extract the second column of the output, which contains the total size of the swap space in MB."
echo "The output of the free command is the total size of the memory swap space (virtual memory) in MB on the VM."

# Question 6 – What is the free disk space of the root disk partition in MB?
printf "\nQuestion 6 – What is the free disk space of the root disk partition in MB?" 
echo "# --------------------------------------------------------------------"
echo "df -m / | tail -1 | awk '{print $4}'"
df -m / | tail -1 | awk '{print $4}'
echo the df command displays disk space usage information,
echo "-m option displays the information in MB, "
echo "and tail -1 filters the output to show only the last line, which contains the information for the root partition."
echo "The awk command is used to extract the fourth column of the output, which contains the free disk space of the root disk partition in MB."
echo "The output of the df command is the free disk space of the root disk partition in MB."

# Question 7 – What is the total number of nodes on the root filesystem?
printf "\nQuestion 7 – What is the total number of nodes on the root filesystem?" 
echo "# --------------------------------------------------------------------"
echo "df -i / | tail -1 | awk '{print $2}'"
df -i / | tail -1 | awk '{print $2}'
echo the df command displays inode usage information,
echo "-i option displays the information in inode, "
echo "and tail -1 filters the output to show only the last line, which contains the information for the root partition."
echo "The awk command is used to extract the second column of the output, which contains the total number of nodes on the root filesystem."
echo "The output of the df command is the total number of nodes on the root filesystem."

# Question 8 – What is the average round trip time (RTT) of 10 ICMP ping packets from your Ubuntu VM to www.google.com?
printf "\nQuestion 8 – What is the average round trip time (RTT) of 10 ICMP ping packets from your Ubuntu VM to www.google.com?" 
echo "# --------------------------------------------------------------------"
echo "ping -c 10 www.google.com | tail -1 | awk -F '/' '{print $5}'"
ping -c 10 www.google.com | tail -1 | awk -F '/' '{print $5}'
echo the ping command sends ICMP echo requests to a specified host,
echo "-c 10 option specifies to send 10 packets, "
echo "and tail -1 filters the output to show only the last line, which contains the average round trip time (RTT) information."
echo "The awk command is used to extract the fifth field of the output, which contains the average round trip time (RTT) of the 10 ICMP ping packets."
echo "The output of the ping command is the average round trip time (RTT) of 10 ICMP ping packets from your Ubuntu VM to www.google.com."

# Question 9 - What is the interface name of the network interface device used to route the ICMP ping packets to www.google.com?
printf "\nQuestion 9 - What is the interface name of the network interface device used to route the ICMP ping packets to www.google.com?" 
echo "# --------------------------------------------------------------------"
echo "ip route get 8.8.8.8 | awk '/dev/ {print $5}'"
ip route get 8.8.8.8 | awk '/dev/ {print $5}'
echo the ip command retrieves routing information for the IP address 8.8.8.8 (Google's public DNS server),      
echo "and awk filters the output to extract the interface name after the 'dev' keyword."
echo "The output of the ip command is the interface name of the network interface device used to route the ICMP ping packets to 8.8.8.8."

# Question 10 – Identify the file system type of the “/” root partition? Briefly describe this file system type (1-2 sentences).
printf "\nQuestion 10 - Identify the file system type of the “/” root partition?" 
echo "# --------------------------------------------------------------------"
echo "df -T / | tail -1 | awk '{print $2}'"
df -T / | tail -1 | awk '{print $2}'
echo the df command displays disk space usage information,
echo "-T option includes the file system type, "
echo "and awk extracts the second column, which contains the file system type."
echo "The output of the df command is the file system type of the root partition."

# BONUS 1 (2 points) Look up 2 Linux commands you are unfamiliar with.
printf "\nBONUS 1 – Look up 2 Linux commands you are unfamiliar with and provide examples.\n"
echo "# --------------------------------------------------------------------"

printf "\nBONUS 2 (2 points) Write a short review (~300 words) about the Ubuntu operating system. What do you think of the UI, installed programs, etc? How does it compare to the OS you're used to? Try installing new programs. How was the overall experience? Then create another VM with a different Linux distribution. Some options include Linux Mint, PopOS, Manjaro, Debian, Fedora, Zorin, CentOS, etc. Write one more short review of that operating system and compare it to Ubuntu. Obvious AI answers that simply regurgitate information on the distribution's website in a bulleted list will not be accepted."
echo "Ubuntu is a great operating system, but not having the access to many of the well written and easy to use tools provided on Windows makes it hard to use as my main driver. It's easy to use and can be fun to feel like a hacker navigating through th ecommand line. I think if I was to commit the time, it could be a valid option as a main driver, but I don't have that kind of time."