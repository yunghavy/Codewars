# algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(array):
    non_zeros = [x for x in array if x != 0 or type(x) == bool]
    zeros = [x for x in array if x == 0 and type(x) != bool]
    return non_zeros + zeros
