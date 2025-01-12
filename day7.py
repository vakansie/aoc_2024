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

def permute_operators(elements: list[int]):
    operator_count = len(elements) - 1
    return list(itertools.product([True, False], repeat = operator_count))

def solve(problem: tuple[int, list[int]]) -> bool:
    answer, elements = problem
    operators = permute_operators(elements)
    for operator in operators:
        total = elements[0]
        for index in range((len(elements) - 1)):
            total = total + elements[index + 1] if operator[index] else total * elements[index + 1]
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