import sys
sys.path.append(r'C:\Users\Person\Desktop\Dr Vaniya Ar\scratch')

from build_b3_u1_u8 import get_b3_units_1_to_8
from build_b3_u9_questions import get_b3_u9_complete_questions
from build_b3_u10_u17 import get_b3_units_10_to_17

b3_all = {}
b3_all.update(get_b3_units_1_to_8())
b3_all[9] = get_b3_u9_complete_questions()
b3_all.update(get_b3_units_10_to_17())

print(f"Total units in Book 3: {len(b3_all)}")
missing_b3 = [i for i in range(1, 18) if i not in b3_all]
print(f"Missing units in Book 3: {missing_b3}")

total_b3_q = 0
for u_num in sorted(b3_all.keys()):
    qs = b3_all[u_num]
    total_b3_q += len(qs)
    tamreens = sorted(list(set(q['tamreen_num'] for q in qs)))
    print(f"  Unit {u_num:2d}: {len(qs):2d} questions, tamreens: {tamreens}")

print(f"\nTotal Book 3 questions: {total_b3_q}")
