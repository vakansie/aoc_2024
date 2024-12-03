import re

file = 'day3-1.txt'

def parse_input() -> str:
    with open(file) as text:
        return text.read()

def parse_memory(memory: str) -> int:
    total = 0
    good_mul_instructions = re.findall('mul\(\d{1,4},\d{1,4}\)', memory)
    print(good_mul_instructions)
    for instruction in good_mul_instructions:
        a, b = instruction[4:-1].split(',')
        total += int(a) * int(b)
    return total

memory = parse_input()
print(parse_memory(memory))