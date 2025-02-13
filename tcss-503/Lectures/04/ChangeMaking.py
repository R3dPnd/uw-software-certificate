'''
*   The goal of this method is, given a target value and a list of denominations, to find the minimum number of coins needed to make the target value.
*   The method will return a list of the coins needed to make the target value.
'''
def change_making_dynamic(target, denoms):
    data = [[]]* (target+1)
    # Loop through each value up to the target
    for i in range(1, target+1):
        curr_min = None
        # Loop through each denomination
        for denom in denoms:
            back_val = i - denom
            # If you are able to subtract the current denomination from the value
            if back_val >= 0:
                # If the previous calculation is invalid and cannot be used
                if data[back_val] == []:
                    continue
                curr = data[back_val].copy()
                curr.append(denom)
                # If the current list of coins is shorter than the current minimum
                if curr_min == None or len(curr) < len(curr_min):
                    curr_min = curr
        data[i] = curr_min