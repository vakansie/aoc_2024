file = 'day5.txt'

def parse_input(file):
    rules = []
    pages = []
    with open(file) as text:
        for line in text:
            if '|' in line:
                first, last = line.split('|')
                rules.append((int(first), int(last)))
            elif line == '\n':
                continue
            else:
                pages.append([int(page) for page in line.split(',')])
    return rules, pages

def check_if_ordered(pages_list):
    unordered_pages = []
    for pages in pages_list:
        ordered = True
        for index, page in enumerate(pages):
            for rule in rules:
                if page == rule[0]:
                    if rule[1] in pages[:index]:
                        ordered = False
                        break
                if page == rule[1]:
                    if rule[0] in pages[index+1:]:
                        ordered = False
                        break
        if not ordered:
            unordered_pages.append(pages)
    return unordered_pages

def sort_page(unordered_pages: list[int]) -> list[int]:

    def sorting_pass(unordered_pages: list[int]) -> list[int]:
        for index, page in enumerate(unordered_pages):
            for rule in rules:
                if page == rule[0]:
                    if rule[1] in unordered_pages[:index]:
                        rule_index = unordered_pages.index(rule[1])
                        unordered_pages[rule_index], unordered_pages[index] = unordered_pages[index], unordered_pages[rule_index]
        return unordered_pages

    sorted = False
    while not sorted:
        if check_if_ordered([unordered_pages]):
            unordered_pages = sorting_pass(unordered_pages)
        else:
            sorted = True
    return unordered_pages

rules, pages_list = parse_input(file)
unordered_pages = check_if_ordered(pages_list)
for page in unordered_pages:
    print(page)
for page in unordered_pages:
    page = sort_page(page)
    print(page)
print(f'middle_sum = {sum([pages[int((len(pages) - 1) / 2)] for pages in unordered_pages])}')