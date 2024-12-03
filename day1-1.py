from collections import Counter

def parse_input()-> tuple[list, list]:
    id_list_1 = []
    id_list_2 = []
    with open('day1-1.txt') as text:
        for line in text:
            id1, id2 = line.split()
            id_list_1.append(int(id1))
            id_list_2.append(int(id2))
    return id_list_1, id_list_2

def compare(a: int, b: int)-> bool:
    return abs(a - b)

def compare_lists(list1: list, list2: list)-> int:
    list1.sort()
    list2.sort()
    compared = list(map(compare, list1, list2))
    return(sum(compared))

def day1():
    list1, list2 = parse_input()
    total = compare_lists(list1, list2)
    print(total)

day1()


def calc_similarity(list1: list, list2: list) -> int:
    similarity_score = 0
    frequencies = Counter(list2)
    for id in list1:
        frequency = frequencies[id]
        similarity_score += (id * frequency)
    return similarity_score

def day2():
    list1, list2 = parse_input()
    similarity_score = calc_similarity(list1, list2)
    print(similarity_score)

day2()