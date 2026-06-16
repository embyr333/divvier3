'''
Objective: Split a collection of numbers (which may 
include replicates) in two, as evenly as possible.
Using iterative superset generation approach to make a collection
of subcollections from which to choose closest-summing pair. 
It will, however, have replicate subcollections, but though 
inefficient I think it will at least allow me to make 
a deterministic split for the 'Divvier' problem, to replace
the original tool which used random sampling to process
larger arrays, so could not guarentee an optimal split.

Snapshot8: Choosing to return a message if single-element list is passed in.

TODO: 
- More tests, checking with original Divvier.
- Maybe change to returning a string as per original program reporting
"Smallest difference found: ---, between subcollection ---, totalling ---
and reciprocal subcollection ---, totalling ---",
or immediately return a message re irrelevance if <2 elements.
- Make GUI
'''

def divvy(nums: list[float]) -> tuple[list[float], list[float]]: 
    if len(nums) < 2: # Exception to return type hint...
        return 'Single-element inputs are not relevant.'

    subcolls: list[list[float]] = [[]]
    for num in nums:
        subcolls += [subcoll + [num] for subcoll in subcolls]
    # Discard first (empty) item and complement (full input); Note1
    subcolls = subcolls[1 : len(subcolls) - 1]
    # print('subcolls', subcolls) # temp check

    subcoll_sums = []
    for subcoll in subcolls:
        subcoll_sums.append(sum(subcoll))
    # print('subcoll_sums', subcoll_sums) # temp check

    total = sum(nums)
    half = total / 2
    # print('total', total, '  half', half) # temp check

    min_offset = total # minimum offset from half (initialise at anything larger than half)
    # ioffm = 0 # index of (first found) minimum offset (from half); Note2
    for i, subcoll_sum in enumerate(subcoll_sums):
        if abs(subcoll_sum - half) < min_offset:
            min_offset = abs(subcoll_sum - half)
            ioffm = i
    # print('min_offset is', min_offset, 'for subcoll', subcolls[ioffm])

    complement = nums.copy() # Note3
    for e in subcolls[ioffm]: # Note4
        complement.remove(e)
    # print('complement', complement) # temp check

    return subcolls[ioffm], complement

'''
Note1: This would need to be removed if single-element inputs 
are possible, and the handling of these with an 'error message'
were not present at the beginning of the function.
Note2: ...Conversely, this would need to be put back.
Note3: Making copy in case we need to avoid modifying the input list.
Shallow copy is sufficient as elements are primitives.
Note4: This is of course time-inefficient.
'''


# Some tests
print(divvy([3,3,7,5,9])) # ([3, 3, 7], [5, 9])
print(divvy([1,2,3])) # ([1, 2], [3])
print(divvy([1,2])) # ([1], [2])
print(divvy([1,2,1,2])) # ([1, 2], [2, 1])
print(divvy([78, 93, 44, 27, 58, 25, 27, 73, 55, 32]))
print(divvy([1])) # Single-element inputs are not relevant.
