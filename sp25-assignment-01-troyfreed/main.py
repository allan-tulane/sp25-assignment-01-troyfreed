"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb
    pass

def longest_run(mylist, key):
    "Create variables that count how long the current run is, and what the highest run has been"
    count = 0
    highest_val = 0
    "Loop through list, if element equals the key raise the count, if not check whether count is the longest run and reset the count "

    for x in mylist:
        if x == key:
            count += 1
        else:
            if count > highest_val:
                highest_val = count
            count = 0
    "Checks if list ends with a run"
    return max(highest_val, count)
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):

    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    "recursively splits"
    middle_point = len(mylist) // 2
    left = longest_run_recursive(mylist[:middle_point], key)
    right = longest_run_recursive(mylist[middle_point:], key)


    "If entire left half is equal to the key, it extends into right half so we add both sizes"
    "If not we just return left size, same thing for the right"

    if left.is_entire_range:
        l_size = left.left_size + right.left_size
    else:
        l_size = left.left_size

    if right.is_entire_range:
        r_size = right.right_size + left.right_size
    else:
        r_size = right.right_size
    " see if longest_run is longest run in left or right half or a run that crossed the boundary"
    longest = max(left.longest_size, right.longest_size, left.right_size + right.left_size)
    entire = left.is_entire_range and right.is_entire_range

    return Result(l_size, r_size, longest, entire)


pass



