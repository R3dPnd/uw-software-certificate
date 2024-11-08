def summary_stats(n):
    """ First calculates the median, and then the average.
    :param n: An array of numeric values.
    :return: A tuple of (median,average)
    """
    # SEGMENT 1 O(1)
    a_len = len(n)
    if a_len == 1: # TRIVIAL CASE WHERE N IS A SINGLE VALUE
        return n[0], n[0]
    
    # SEGMENT 2 O(nlog(n))
    a = merge_sort(n) # USE WHAT YOU KNOW ABOUT TIME COMPLEXITY OF MERGE SORT FOR THIS SEGMENT
    
    # SEGMENT 3 T(1)
    split = a_len // 2
    median: int = 0
    if a_len % 2 == 0: # is even
        median = (a[split - 1] + a[split]) / 2
    else:
        median = a[split]
        
    # SEGMENT 4 T(n)
    running_sum = 0
    for i in range(0, a_len):
        running_sum += a[i]
        mean = running_sum / a_len
    return (median, mean)

l = [1,7,4,2,1,4,3,6,7,3,12,40]
med, avg = summary_stats(l)
print(med)
print(avg)