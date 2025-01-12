import itertools 

file = r'day7.txt'

def parse_input(file):
    with open(file) as text:
        problems = []
        for line in text:
            answer, elements = line.split(':')
            answer, elements = int(answer), list(elements.strip().split(' '))
            elements = [int(element) for element in elements]
            print(f'{answer = } {elements = }')
            problems.append((answer, elements))
        return problems

def addr(a, b):
    return a + b

def mult(a, b):
    return a * b

def conj(a, b):
    return int(str(a) + str(b))

def permute_operators(elements: list[int]):
    operator_count = len(elements) - 1
    return list(itertools.product([addr, mult, conj], repeat = operator_count))

def solve(problem: tuple[int, list[int]]) -> bool:
    answer, elements = problem
    operator_permutations = permute_operators(elements)
    for operators in operator_permutations:
        total = elements[0]
        for index in range((len(elements) - 1)):
            total = operators[index](total, elements[index + 1])
        if total == answer:
            return True
    return False

problems = parse_input(file)
summ = 0
for problem in problems:
    if solve(problem):
        print(f'valid: {problem}')
        summ += problem[0]
    else: print(f'invalid: {problem}')
print(f'{summ = }')