import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\.gemini\antigravity\brain\871510d4-1766-4c62-b894-0270b402a9f3\madinah_curriculum_tamreens_manifest.md', encoding='utf-8') as f:
    text = f.read()

lines = [l for l in text.splitlines() if l.startswith('| Book ')]

# Sample Lesson 1 of Book 2
b2_l1 = [l for l in lines if 'Book 2, Lesson 1:' in l]
print("=== BOOK 2 LESSON 1 MANIFEST ROWS ===")
for r in b2_l1:
    print(r)

# Sample Lesson 1 of Book 3
b3_l1 = [l for l in lines if 'Book 3, Lesson 1:' in l]
print("\n=== BOOK 3 LESSON 1 MANIFEST ROWS ===")
for r in b3_l1:
    print(r)
