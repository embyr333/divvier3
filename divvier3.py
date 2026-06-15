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

Snapshot6: --fixed bug; added a few more tests.

TODO: 
- More tests, checking with original Divvier.
- Maybe change to returning a string as per original program reporting
"Smallest difference found: ---, between subcollection ---, totalling ---
and reciprocal subcollection ---, totalling ---",
or immediately return a message re irrelevance if <2 elements.
- Make GUI
'''

def divvy(nums: list[float]) -> tuple[list[float], list[float]]: 

    subcolls: list[list[float]] = [[]]
    for num in nums:
        subcolls += [subcoll + [num] for subcoll in subcolls]
    # Discard first (empty) item and complement (full input); (optional)
    subcolls = subcolls[1 : len(subcolls) - 1]
    # print('subcolls', subcolls) # temp check

    subcoll_sums = []
    for subcoll in subcolls:
        subcoll_sums.append(sum(subcoll))
    # print('subcoll_sums', subcoll_sums) # temp check

    total = sum(nums)
    half = total / 2
    # print('half', half) # temp check

    min_offset = total # minimum offset from half (initialise at anything larger than half)
    ioffm = 0 # index of (first found) minimum offset (from half); Note1
    for i, subcoll_sum in enumerate(subcoll_sums):
        if abs(subcoll_sum - half) < min_offset:
            min_offset = abs(subcoll_sum - half)
            ioffm = i
    # print('min_offset is', min_offset, 'for subcoll', subcolls[ioffm])

    # Now find a 'complement', i.e. a subset whose sum 
    # with that of subcolls[ioffm] add to sum(input)
    ioffc = 0 # index of (first found) complement
    for i, subcoll_sum in enumerate(subcoll_sums):
        if sum(subcolls[ioffm]) + subcoll_sum == total and i != ioffm: # --added condition to fix bug
            ioffc = i
            break
    # print('complement is', subcolls[ioffc]) 

    return subcolls[ioffm], subcolls[ioffc]

# Note1: Can discard this pre-declaration/initialisation 
# outside loop when input length > 1 is enforced


# Some tests
print(divvy([3,3,7,5,9])) # ([3, 3, 7], [5, 9])
print(divvy([1,2,3])) # ([1, 2], [3])
print(divvy([1,2])) # ([1], [2])
print(divvy([1,2,1,2])) # ([1, 2], [2, 1])
