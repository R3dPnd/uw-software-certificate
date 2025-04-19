#!/bin/bash

# Parse command-line arguments
VERBOSE=false
while getopts "v" opt; do
  case $opt in
    v) VERBOSE=true ;;
    *) echo "Usage: $0 [-v]"; exit 1 ;;
  esac
done

# Question 1 – How many total processes are present shortly after the Ubuntu VM boots up?
echo "Question 1 – How many total processes are present shortly after the Ubuntu VM boots up?"
echo "# --------------------------------------------------------------------"
echo "ps -e | wc -l"
ps -e | wc -l
if [ "$VERBOSE" = true ]; then
  echo "The ps command lists out the running processes,"
  echo "-e option lists all processes,"
  echo "and wc -l counts the number of lines in the output."
fi

# Question 2 – How many total threads are present shortly after the Ubuntu VM boots up?
echo ""
echo "Question 2 – How many total threads are present shortly after the Ubuntu VM boots up?"
echo "# --------------------------------------------------------------------"
echo "ps -eLf | wc -l"
ps -eLf | wc -l
if [ "$VERBOSE" = true ]; then
  echo "The ps command lists out the running processes,"
  echo "-e option lists all processes,"
  echo "-L option lists all threads,"
  echo "and wc -l counts the number of lines in the output."
  echo "The output of the ps command is piped to wc -l to count the number of lines, which gives the total number of threads."
fi

# Question 3 – What is the version number of the Linux kernel installed on your Ubuntu VM?
echo ""
echo "Question 3 – What is the version number of the Linux kernel installed on your Ubuntu VM?"
echo "# --------------------------------------------------------------------"
echo "uname -r"
uname -r
if [ "$VERBOSE" = true ]; then
  echo "The uname command prints system information,"
  echo "-r option prints the kernel version number."
  echo "The output of the uname command is the version number of the Linux kernel installed on the system."
fi

# Question 4 – What is the model name of the CPU(s) of the VM?
echo ""
echo "Question 4 – What is the model name of the CPU(s) of the VM?"
echo "# --------------------------------------------------------------------"
echo "lscpu | grep 'Model name'"
lscpu | grep "Model name"
if [ "$VERBOSE" = true ]; then
  echo "The lscpu command prints CPU architecture information,"
  echo "and grep 'Model name' filters the output to show only the model name of the CPU(s)."
fi

# Question 5 – What is the total size of the memory swap space (virtual memory) in MB on the VM?
echo ""
echo "Question 5 – What is the total size of the memory swap space (virtual memory) in MB on the VM?"
echo "# --------------------------------------------------------------------"
echo "free -m | grep 'Swap' | awk '{print $2}'"
free -m | grep "Swap" | awk '{print $2}'
if [ "$VERBOSE" = true ]; then
  echo "The free command displays memory usage information,"
  echo "-m option displays the information in MB,"
  echo "and grep 'Swap' filters the output to show only the swap space information."
  echo "The awk command is used to extract the second column of the output, which contains the total size of the swap space in MB."
fi

# Question 6 – What is the free disk space of the root disk partition in MB?
echo ""
echo "Question 6 – What is the free disk space of the root disk partition in MB?"
echo "# --------------------------------------------------------------------"
echo "df -m / | tail -1 | awk '{print $4}'"
df -m / | tail -1 | awk '{print $4}'
if [ "$VERBOSE" = true ]; then
  echo "The df command displays disk space usage information,"
  echo "-m option displays the information in MB,"
  echo "and tail -1 filters the output to show only the last line, which contains the information for the root partition."
  echo "The awk command is used to extract the fourth column of the output, which contains the free disk space of the root disk partition in MB."
fi

# Question 7 – What is the total number of nodes on the root filesystem?
echo ""
echo "Question 7 – What is the total number of nodes on the root filesystem?"
echo "# --------------------------------------------------------------------"
echo "df -i / | tail -1 | awk '{print $2}'"
df -i / | tail -1 | awk '{print $2}'
if [ "$VERBOSE" = true ]; then
  echo "The df command displays node usage information,"
  echo "-i option displays the information in node,"
  echo "and tail -1 filters the output to show only the last line, which contains the information for the root partition."
  echo "The awk command is used to extract the second column of the output, which contains the total number of nodes on the root filesystem."
fi

# Question 8 – What is the average round trip time (RTT) of 10 ICMP ping packets from your Ubuntu VM to www.google.com?
echo ""
echo "Question 8 – What is the average round trip time (RTT) of 10 ICMP ping packets from your Ubuntu VM to www.google.com?"
echo "# --------------------------------------------------------------------"
echo "ping -c 10 www.google.com | tail -1 | awk -F '/' '{print $5}'"
ping -c 10 www.google.com | tail -1 | awk -F '/' '{print $5}'
if [ "$VERBOSE" = true ]; then
  echo "The ping command sends ICMP echo requests to a specified host,"
  echo "-c 10 option specifies to send 10 packets,"
  echo "and tail -1 filters the output to show only the last line, which contains the average round trip time (RTT) information."
  echo "The awk command is used to extract the fifth field of the output, which contains the average round trip time (RTT) of the 10 ICMP ping packets."
fi

# Question 9 - What is the interface name of the network interface device used to route the ICMP ping packets to www.google.com?
echo ""
echo "Question 9 - What is the interface name of the network interface device used to route the ICMP ping packets to www.google.com?"
echo "# --------------------------------------------------------------------"
echo "ip route get 8.8.8.8 | awk '/dev/ {print $5}'"
ip route get 8.8.8.8 | awk '/dev/ {print $5}'
if [ "$VERBOSE" = true ]; then
  echo "The ip command retrieves routing information for the IP address 8.8.8.8 Google's public DNS server,"
  echo "and awk filters the output to extract the interface name after the 'dev' keyword."
fi

# Question 10 – Identify the file system type of the “/” root partition? Briefly describe this file system type (1-2 sentences).
echo ""
echo "Question 10 - Identify the file system type of the “/” root partition?"
echo "# --------------------------------------------------------------------"
echo "df -T / | tail -1 | awk '{print $2}'"
df -T / | tail -1 | awk '{print $2}'
if [ "$VERBOSE" = true ]; then
  echo "The df command displays disk space usage information,"
  echo "-T option includes the file system type,"
  echo "tail -1 filters the output to show only the last line, which contains the information for the root partition."
  echo "awk extracts the second column, which contains the file system type."
  echo "The output of the df command is the file system type of the root partition."
fi

# BONUS 1 (2 points) Look up 2 Linux commands you are unfamiliar with.
echo ""
echo "BONUS 1 – Look up 2 Linux commands you are unfamiliar with and provide examples."
echo "# --------------------------------------------------------------------"
echo "1. awk - A command-line utility for processing and analyzing text files. It is commonly used for pattern scanning and processing."
echo "Example: awk '{print $1}' file.txt - This command prints the first column of each line in the file.txt file."
echo "2. df - A command-line utility that displays information about disk space usage on file systems."
echo "Example: df -h - This command displays disk space usage in a human-readable format (e.g., MB, GB)."
