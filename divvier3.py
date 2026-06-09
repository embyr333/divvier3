'''
Snapshot1: Coming across approach for making supersets 

After quickly reading NeetCode 'Intuition' description of his 
2nd solution (no-tree-as-such) iteration approach I realises this 
at least might be doable for me without further assistance.
Horrified I hadn't though of it myself!
His code is more concise though - single-loop-single-line!
'''

# from copy import deepcopy
def subsetsMine(nums: list[int]) -> list[list[int]]:
    coll = [[]] # collection of subsets so far
    for num in nums:
        # new = deepcopy(coll)
        # ...or can do...
        new = [sublist[:] for sublist in coll]
        # ...or slight variant, seen afterwards...
        # new = [list(sublist) for sublist in coll]
        for i in range(len(new)):
            new[i].append(num)
        coll.extend(new)
    return coll

print(subsetsMine([1,2,3]), '\n') # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsetsMine([7]), '\n') # [[],[7]]


def subsetsNC(nums: list[int]) -> list[list[int]]:
    res = [[]]

    for num in nums:
        res += [subset + [num] for subset in res]

    return res

print(subsetsNC([1,2,3]), '\n') # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsetsNC([7]), '\n') # [[],[7]]