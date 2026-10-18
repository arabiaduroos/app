import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch_b1_dump.txt', 'r', encoding='utf-8') as f:
    text = f.read()

units = re.split(r'=== UNIT (\d+)[^=]*===', text)
print(f"Total parts in scratch_b1_dump: {len(units)}")

for i in range(1, len(units), 2):
    u_num = units[i]
    u_content = units[i+1].strip()
    lines = u_content.split('\n')
    print(f"\n--- UNIT {u_num} ({len(lines)} lines) ---")
    for l in lines[:15]:
        print(" ", l[:80])
