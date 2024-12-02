def get_sub_report(report: list[int], index_to_remove: int):
    return report[:index_to_remove] + report[index_to_remove+1:]

def iterate_sub_reports(report: list[int]):
    for i in range(len(report)):
        sub_report = get_sub_report(report, i)
        if check_if_safe(sub_report, has_damp_been_used=True):
            return True
    return False

def check_if_safe(report: list[int], has_damp_been_used = False) -> bool:
    if len(report) == 1: return True
    is_desc = report[0] > report[1]
    for i, level in enumerate(report):
        if i == len(report) - 1: continue
        next_level = report[i+1]
        if is_desc and level <= next_level:
            if has_damp_been_used: return False
            return iterate_sub_reports(report)
        if not is_desc and level >= next_level:
            if has_damp_been_used: return False
            return iterate_sub_reports(report)
        if level == next_level: 
            if has_damp_been_used: return False
            return iterate_sub_reports(report)
        if abs(level - next_level) > 3: 
            if has_damp_been_used: return False
            return iterate_sub_reports(report)
    return True


safe_count = 0
with open("input.txt", 'r') as input:
    reports = [[int(level) for level in raw_report.split()] for raw_report in input.readlines()]
    for report in reports:
        if check_if_safe(report):
            safe_count += 1

print(safe_count)