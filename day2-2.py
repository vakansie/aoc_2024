file = 'day2-1.txt'

def parse_input() -> list[int]:
    safe_count = 0
    with open(file) as text:
        for line in text:
            report = list(map(int, line.split()))
            # print(report)
            if is_safe(report): safe_count += 1
    return safe_count

def create_subreports(report: list[int]) -> list[list[int]]:
    subreports = []
    for index, value in enumerate(report):
        subreport = report.copy()
        subreport.pop(index)
        subreports.append(subreport)
    return subreports


def is_safe(report: list[int]) -> bool:
    def is_sub_safe(subreport: list[int]) -> bool:
        for index, value in enumerate(subreport):
            if index + 1 == len(subreport): break
            if not 0 < abs(value - subreport[index + 1]) < 4:
                return False
        asc = subreport.copy()
        asc.sort()
        desc = asc.copy()
        desc.reverse()
        if subreport != asc and subreport != desc:
            return False
        print(subreport)
        return True
    sub_reports = create_subreports(report)
    return any(list(map(is_sub_safe, sub_reports)))

    

safe_count = parse_input()
print(safe_count)