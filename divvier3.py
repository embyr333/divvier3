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

Snapshot13: Arranged to display error message in output field for invalid input.

TODO: 
- Maybe: add a Clear button to GUI; disable editing of output (though not copying).
- Make an executable.
'''

import re

# If using CLI
# def divvy(nums: list[float]) -> str: 

# If using GUI
def divvy(): # if using GUI
    text = input_field.get("1.0",'end').rstrip() 
    output_field.delete('1.0', END) # clear any existing output
    try:
        nums: list[float] = [float(x) for x in re.split(r"[,\s]+", text)]
    except ValueError: 
        output_field.insert("end", 'Invalid input - please enter only numbers\n'
        '(separated only by whitespace and/or commas)')

    if len(nums) < 2: 
        return 'Input lists smaller than 2 numbers are not relevant.\n'

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

    min_offset = float('inf') # minimum offset from half 

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
 
    report = ('Smallest difference found: ' + str(abs(subcoll_sums[ioffm] - sum(complement))) + '\n' +
    'between subcollection ' + str(subcolls[ioffm]) + '\n' +
    '(totalling ' + str(subcoll_sums[ioffm])  + ')\n' +
    'and complement        ' + str(complement) + '\n' 
    '(totalling ' + str(sum(complement))  + ')\n' +
    '(Other combinations may exist.)\n')

    # If using CLI
    # return report

    # If using GUI
    output_field.insert("end", report)

'''
Note1: This would need to be removed if single-element inputs 
are possible, and the handling of these with an 'error message'
were not present at the beginning of the function.
Note2: ...Conversely, this would need to be put back.
Note3: Making copy in case we need to avoid modifying the input list.
Shallow copy is sufficient as elements are primitives.
Note4: This is of course time-inefficient.
'''


# Some tests, with smallest difference noted 
# print(divvy([])) # Input lists smaller than 2 numbers are not relevant.
# print(divvy([1])) # Input lists smaller than 2 numbers are not relevant.
# print(divvy([3,3,7,5,9])) # 1 
# print(divvy([1,2,3])) # 0
# print(divvy([1,2])) # 1 
# print(divvy([1,2,1,2])) # 0 
# print(divvy([78, 93, 44, 27, 58, 25, 27, 73, 55, 32])) # 0 
# print(divvy([880, 953, 229, 77, 96, 37, 7, 30, 18, 2])) # 1 
# print(divvy([378, 222, 1, 83, 704, 6, 129, 455, 22, 97])) # 5
# print(divvy([378, 222, 1, 83, 704, 378, 222, 1, 83, 704])) # 0
# print(divvy([378, 222, 1, 83, 704, 378, 222, 1, 83, 704, 378, 222, 1, 83, 704])) # 10
# print(divvy([1.5,2.5,0.5,4.5])) # 0.0
# print(divvy([1,-2,-1,2])) # 0 


# GUI...

from tkinter import *
from tkinter.scrolledtext import ScrolledText
root_widget = Tk()
root_widget.title("divvier3 splits a collection of numbers in two as evenly as possible")
root_widget.geometry("690x570") # provisional width, height GUI

Label(root_widget, text = 'Enter list of numbers separated by commas and/or whitespace').grid(row=0, column=0) 

input_field = ScrolledText(root_widget, width = 80, fg = 'blue', font=("Courier", 10), height=15) 
input_field.grid(row=1, column=0, padx=15) 

output = StringVar()

submit_button = Button(root_widget, text = 'Submit', command = lambda: divvy(), bg='#C8C8C8')
submit_button.grid(row=2, column=0)

output_field = ScrolledText(root_widget, width = 80, fg = 'blue', font=("Courier", 10), height=15) 
output_field.grid(row=3, column=0) 

root_widget.mainloop()