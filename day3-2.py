import re

file = 'day3-1.txt'

def parse_input() -> str:
    memory = ''
    with open(file) as text:
        for line in text:
            memory += line
            print(f'{memory = }')
    return memory

def parse_memory(memory: str) -> int:
    total = 0
    instructions = re.findall("mul\(\d{1,4},\d{1,4}\)|do\(\)|don't\(\)", memory)
    print(instructions)

    do = True
    for instruction in instructions:
        if instruction == "don't()":
            do = False
        elif instruction == "do()":
            do = True
        elif do:
            a, b = instruction[4:-1].split(',')
            total += int(a) * int(b)
    return total

memory = parse_input()
print(parse_memory(memory))