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

def check_if_ordered(rules, pages_list):
    ordered_pages = []
    for pages in pages_list:
        ordered = True
        for index, page in enumerate(pages):
            for rule in rules:
                if page == rule[0]:
                    if rule[1] in pages[:index]:
                        ordered = False
                if page == rule[1]:
                    if rule[0] in pages[index+1:]:
                        ordered = False
        if ordered:
            ordered_pages.append(pages)
    middle_sum = sum([pages[int((len(pages) - 1) / 2)] for pages in ordered_pages])
    return middle_sum, ordered_pages

rules, pages_list = parse_input(file)
print(rules)
print(pages_list)
middle_sum, ordered_pages = check_if_ordered(rules, pages_list)
for page in ordered_pages:
    print(page)
print(middle_sum)