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

Snapshot4: Minor changes.
TODO: Tidy up, make an 'array -> best split function', GUI.
'''
# def subcolls_gen(nums: list[float]) -> list[list[float]]: 
# (Changed input element type hint to float to indicate  
# elements do not have to be ints)
def subcolls_gen(nums: list[float]) -> list[list[float]]: 
    subcolls: list[list[float]] = [[]]
    for num in nums:
        subcolls += [subcoll + [num] for subcoll in subcolls]
    return subcolls

input = [3,3,7,5,9]

total = sum(input)

subcolls = subcolls_gen(input)
# Discard first (empty) item and complement (full input); (optional)
subcolls = subcolls[1 : len(subcolls) - 1]
print('subcolls', subcolls) # temp check

subcoll_sums = []
for subcoll in subcolls:
    subcoll_sums.append(sum(subcoll))
print('subcoll_sums', subcoll_sums) # temp check

half = total / 2
print('half', half) # temp check
min_offset = total # minimum offset from half 
# (initialise at anything larger than half)
# ioffmo = 0 # index of (first found) minimum offset (from half)
# ...typo (which does not interfere unless input has just single element)
ioffm = 0 # index of (first found) minimum offset (from half)
# ...can discard this when input length > 1 is enforced)

for i, subcoll_sum in enumerate(subcoll_sums):
    if abs(subcoll_sum - half) < min_offset:
        min_offset = abs(subcoll_sum - half)
        ioffm = i

print('min_offset is', min_offset, 'for subcoll', subcolls[ioffm])
# min_offset is 0.5 for subcoll [3, 3, 7]

# Now find a 'complement', i.e. a subset whose sum 
# with that of subcolls[ioffm] add to sum(input)
ioffc = 0 # index of (first found) complement
for i, subcoll_sum in enumerate(subcoll_sums):
    if sum(subcolls[ioffm]) + subcoll_sum == total:
        ioffc = i
        break
print('complement is', subcolls[ioffc]) 
# complement is [5, 9]
