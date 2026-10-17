# -*- coding: utf-8 -*-
"""
Master Curriculum for Madinah Book 2 (Units 1 to 31)
Combines Part 1 (1-5), Part 2 (6-15), and Part 3 (16-31).
All questions authentic, Tashkeel-rich, with Urdu and English translations.
"""
import sys

from b2_part1_units import get_b2_part1
from build_b2_u6_u15_deep import get_b2_units_6_to_15
from build_b2_u16_u31_deep import get_b2_units_16_to_31

def get_b2_master_curriculum():
    curriculum = {}
    
    # 1. Units 1 to 5
    p1 = get_b2_part1()
    curriculum.update(p1)
    
    # 2. Units 6 to 15
    p2 = get_b2_units_6_to_15()
    curriculum.update(p2)
    
    # 3. Units 16 to 31
    p3 = get_b2_units_16_to_31()
    curriculum.update(p3)
    
    # Verify all 31 units present and assign strict unique IDs
    for u_num in range(1, 32):
        if u_num not in curriculum or len(curriculum[u_num]) == 0:
            raise ValueError(f"Book 2 Unit {u_num} is missing or empty!")
        qs = curriculum[u_num]
        for idx, q in enumerate(qs, 1):
            q["id"] = f"b2_u{u_num}_q{idx}"
            q["book"] = 2
            q["unit_num"] = u_num
            
    return curriculum

if __name__ == '__main__':
    c = get_b2_master_curriculum()
    print("Book 2 Master Curriculum built successfully!")
    print(f"Total units: {len(c)}")
    total = sum(len(qs) for qs in c.values())
    print(f"Total questions: {total}")
    for u_num in sorted(c.keys()):
        tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in c[u_num])))
        print(f"  Unit {u_num:2d}: {len(c[u_num]):2d} questions | Tamreens: {tamreens}")
