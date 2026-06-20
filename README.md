# divvier3

Quite a while ago, after being in a situation where I wanted to divide up some edible items by weight into two equal-as-possible parts, I made my original ‘Divvier’ tool (https://github.com/embyr333/Divvier). Its goal: to divide a collection of numbers, which may include replicates, into two subcollections as evenly as possible, i.e. so the sums of the two subcollections are as close as possible.

At the time, I wrote “There are probably equivalent or better tools out there, but I couldn't come up with sufficiently specific search phrasings to find them”. I suspected the problem would be trivial for computer science practitioners, but ended up using random sampling for larger collection sizes.

Thinking I would probably come across a better approach, that would allow fully deterministic outputs, ‘organically’ at some point, I avoided asking chatbots when they started to have opinions on such matters. Then, a little while ago, seeing a description for making a superset iteratively made me think “Why didn’t I think of that?” Not ideal, as applying it to a collection with replicate elements means there will be replicate (equivalent, order not important) subcollections in the ‘supercollection’, but still something worth making before trying to improve efficiency.
 
Limitation: Because of the exponential growth of subcollection number with input size, 
the algorithm is not practical for processing inputs above approx. 20 elements on my laptop.

Update: Have now made a version 'divvier3b' that might be expected to be a bit more more efficient, and was a little faster on 5 of the 7 input lists crudely tested against this program - see Word file "divvier3 vs 3b".