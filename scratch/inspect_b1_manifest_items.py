import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\.gemini\antigravity\brain\871510d4-1766-4c62-b894-0270b402a9f3\madinah_curriculum_tamreens_manifest.md', encoding='utf-8') as f:
    text = f.read()

lines = [l for l in text.splitlines() if l.startswith('| Book 1')]
print(f"Book 1 has {len(lines)} items in manifest.")
for l in lines[40:70]:
    parts = [p.strip() for p in l.split('|')[1:-1]]
    print(f"{parts[0][:25]} | {parts[1]} | {parts[2]} | {parts[4]}")
