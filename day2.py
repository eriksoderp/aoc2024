with open('input2.txt') as f: lines = f.readlines()
reports = [list(map(int, line.split())) for line in lines]

def is_safe(report):
    increasing = None
    for i, level in enumerate(report):
        if i == len(report) - 1: return 1

        if abs(level - report[i+1]) > 3 or level == report[i+1]:
            return 0
        elif level - report[i+1] >= 1:
            if increasing is None: increasing = False
            elif increasing: return 0
        elif report[i+1] - level >= 1:
            if increasing is None: increasing = True
            elif not increasing: return 0

# part 1
print(sum(is_safe(report) for report in reports))

# part 2
def all_reports(report):
    reports = []
    for i, _ in enumerate(report):
        if i == len(report): break
        reports.append(report[:i] + report[i+1:])
    return reports

all_reports = list(map(all_reports, reports))
print(sum([any(is_safe(r)==1 for r in rs) for rs in all_reports]))
