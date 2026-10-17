import sys
sys.path.append(r'C:\Users\Person\Documents\GitHub\app\scratch')

from b2_part1_units import get_b2_part1
from b2_part2_units import get_b2_part2
from b2_part3_units import get_b2_part3

p1 = get_b2_part1()
p2 = get_b2_part2()
p3 = get_b2_part3()

print(f"Part 1 units: {list(p1.keys())}")
print(f"Part 2 units: {list(p2.keys())}")
print(f"Part 3 units: {list(p3.keys())}")

all_b2 = {}
all_b2.update(p1)
all_b2.update(p2)
all_b2.update(p3)

print(f"\nTotal Book 2 units covered: {len(all_b2)}")
for u_num in sorted(all_b2.keys()):
    qs = all_b2[u_num]
    tamreens = sorted(list(set(q['tamreen_num'] for q in qs)))
    print(f"  Unit {u_num:2d}: {len(qs):2d} questions, tamreens: {tamreens}")
