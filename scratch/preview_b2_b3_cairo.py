import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b2_text = text[b2_idx:b3_idx]
b3_text = text[b3_idx:]

b2_sections = re.split(r'\n###\s+', b2_text)
b3_sections = re.split(r'\n###\s+', b3_text)

print(f"Book 2 sections: {len(b2_sections)-1}")
print(f"Book 3 sections: {len(b3_sections)-1}")

# Check first section of Book 2
print("\n--- Book 2 Lesson 1 Preview ---")
print("\n".join(b2_sections[1].split('\n')[:35]))

# Check first section of Book 3
print("\n--- Book 3 Lesson 1 Preview ---")
print("\n".join(b3_sections[1].split('\n')[:35]))
