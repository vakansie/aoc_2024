file = 'day2-1.txt'

def parse_input() -> list[int]:
    safe_count = 0
    with open(file) as text:
        for line in text:
            report = list(map(int, line.split()))
            if is_safe(report): safe_count += 1
    return safe_count

def is_safe(report: list[int]) -> bool:
    for index, value in enumerate(report, 1):
        if index == len(report): break
        if not 0 < abs(value - report[index]) < 4:
            return False
    asc = report.copy()
    asc.sort()
    desc = asc.copy()
    desc.reverse()
    if report != asc and report != desc:
        return False
    print(report)
    return True

safe_count = parse_input()
print(safe_count)