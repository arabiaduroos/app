# -*- coding: utf-8 -*-
"""
Master Curriculum for Madinah Book 3 (Units 1 to 17)
Combines Units 1-2, 3-4, 5-8 (expanded), Unit 9 (gold standard 93 questions), and Units 10-17 (deep + complete).
All questions authentic, Tashkeel-rich, with Urdu and English translations.
"""
import sys

from build_b3_full_units import get_b3_complete_dataset
from expand_b3_u3_u8 import get_b3_u3_u8_expanded
from build_b3_u10_u17_deep import get_b3_units_10_to_17_deep
from build_b3_u10_u17_complete import get_b3_units_10_to_17_complete

def get_b3_master_curriculum():
    master = {}
    
    # 1. Base dataset (Units 1-8 and Unit 9 gold standard)
    base = get_b3_complete_dataset()
    master.update(base)
    
    # 2. Expand Units 5 to 8
    exp_5_8 = get_b3_u3_u8_expanded()
    for u_id, extra_qs in exp_5_8.items():
        if u_id in master:
            # Combine without duplicating content
            existing_prompts = set(q['prompt_ar'] for q in master[u_id])
            for q in extra_qs:
                if q['prompt_ar'] not in existing_prompts:
                    master[u_id].append(q)
                    existing_prompts.add(q['prompt_ar'])
        else:
            master[u_id] = extra_qs

    # 3. Units 10 to 17: Deep base + Complete dialogue & rules
    u10_17_deep = get_b3_units_10_to_17_deep()
    u10_17_comp = get_b3_units_10_to_17_complete()
    for u_num in range(10, 18):
        u_id = f"b3_u{u_num}"
        combined = []
        seen_prompts = set()
        
        # Dialogue questions first from complete
        if u_id in u10_17_comp:
            for q in u10_17_comp[u_id]:
                if q['prompt_ar'] not in seen_prompts:
                    combined.append(q)
                    seen_prompts.add(q['prompt_ar'])
                    
        # Grammar exercises from deep
        if u_id in u10_17_deep:
            for q in u10_17_deep[u_id]:
                if q['prompt_ar'] not in seen_prompts:
                    combined.append(q)
                    seen_prompts.add(q['prompt_ar'])
                    
        master[u_id] = combined

    # 4. Global re-indexing and strict ID validation
    for u_num in range(1, 18):
        u_id = f"b3_u{u_num}"
        if u_id not in master or len(master[u_id]) == 0:
            raise ValueError(f"Book 3 Unit {u_id} is missing or empty!")
        qs = master[u_id]
        for idx, q in enumerate(qs, 1):
            q["id"] = f"b3_u{u_num}_q{idx}"
            q["book"] = 3
            q["unit_num"] = u_num

    return master

if __name__ == '__main__':
    m = get_b3_master_curriculum()
    print("Book 3 Master Curriculum built successfully!")
    print(f"Total units: {len(m)}")
    total = sum(len(qs) for qs in m.values())
    print(f"Total questions: {total}")
    for u_num in range(1, 18):
        u_id = f"b3_u{u_num}"
        qs = m[u_id]
        tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in qs)))
        print(f"  Unit {u_num:2d} ({u_id}): {len(qs):2d} questions | Tamreens: {tamreens}")
