import sys

a, b, c, d = sys.stdin.readline()[:-1]
ops = ['-', '+']
for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            stmt = f'{a}{op1}{b}{op2}{c}{op3}{d}'
            if eval(stmt) == 7:
                print(f'{stmt}=7')
                exit()
