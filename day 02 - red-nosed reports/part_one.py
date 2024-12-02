def check_if_safe(report: list[int]) -> bool:
    if len(report) == 1: return True
    is_desc = report[0] > report[1]
    for i, level in enumerate(report):
        if i == len(report) - 1: continue
        next_level = report[i+1]
        if is_desc and level <= next_level: return False
        if not is_desc and level >= next_level: return False
        if level == next_level: return False
        if abs(level - next_level) > 3: return False
    return True


safe_count = 0
with open("input.txt", 'r') as input:
    reports = [[int(level) for level in raw_report.split()] for raw_report in input.readlines()]
    for report in reports:
        if check_if_safe(report):
            safe_count += 1

print(safe_count)