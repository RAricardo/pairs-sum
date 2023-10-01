# O(n) solution
def pairs_sum(array, target_sum):
    complements = set()  # Key: Complement of target_sum - current_value, Value: current_value. 
    res = [] # results list
    for num in array:
        complement = target_sum - num
        # If a complement is stored in the map, it means it can be added to num to get the target value.
        if num in complements:
            res.append([num, complement])
        else:
            # If it's not present, we hash num to its target_sum complement.
            complements.add(complement)
    return res