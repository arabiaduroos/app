import sys
import re

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all books (##)
books = re.findall(r'^##\s+(.*?)$', text, re.MULTILINE)
print("Books found:")
for b in books:
    sys.stdout.buffer.write(f"  {b}\n".encode('utf-8'))

# Find all lessons (###)
lessons = re.findall(r'^###\s+(.*?)$', text, re.MULTILINE)
print(f"\nTotal lessons found: {len(lessons)}")
for i, l in enumerate(lessons):
    sys.stdout.buffer.write(f"  Lesson {i+1}: {l}\n".encode('utf-8'))
