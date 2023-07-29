'''Jane's family has just moved to a new city and today is her first day of school. She has a
list of instructions for walking from her home to the school. Each instruction describes a
turn she must make. For example, the list
R
QUEEN
R
FOURTH
R
SCHOOL
means that she must turn right onto Queen Street, then turn right onto Fourth Street, then
finally turn right into the school. Your task is to write a computer program which will
create instructions for walking in the opposite direction: from her school to her home.
The input and output for your program will be formatted like the samples below. You
may assume that Jane's list contains at least two but at most five instructions, and you
may assume that each line contains at most 10 characters, all of them capital letters. The
last instruction will always be a turn into the "SCHOOL'''


def reverse_instructions(instructions):
    instructions.reverse()
    reversed_instructions = []
    index = 1
    for instruction in instructions:
        if index % 2 == 0:
            if instruction == "R":
                reversed_instructions.append('L')
            elif instruction == 'L':
                reversed_instructions.append('R')
        else:
            reversed_instructions.append(instruction)
        index +=1
    street_names = [reversed_instructions[i] for i in range(len(reversed_instructions)) if i % 2 == 0]
    #li = last_elem = reversed_instructions[-1:][0]

    index1 = 0
    streetindex = 1
    for instruction in reversed_instructions:
        if index1 % 2 == 0 and 0 <= index1 < len(reversed_instructions) - 1:
            if instruction == 'L':
                print(f"Turn LEFT onto {street_names[streetindex]} street")
                streetindex +=1
            elif instruction == 'R':
                print(f"Turn RIGHT onto {street_names[streetindex]} street")
                streetindex+=1
        elif index1 == len(reversed_instructions):
            if instruction == 'L':
                print(f"Turn LEFT into your HOME")
            elif instruction == 'R':
                print(f"Turn RIGHT into your HOME")
        index1 +=2
# Assuming the input is space-separated instructions
instructions = input().split()

reverse_instructions(instructions)