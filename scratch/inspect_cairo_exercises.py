import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo = f.read()

# Let's see some sample exercises from Book 1, Book 2, Book 3
print("=== SAMPLE BOOK 1 EXERCISES ===")
b1_matches = re.findall(r'(\([0-9]+\)\s*(?:أجب|اقرأ|اِقْرَأْ|كون|أضف|صَحِّحْ|ضع|هات).*?)(?=\n\([0-9]+\)|\n####|\n---|\Z)', cairo, re.DOTALL)
print(f"Book 1 pattern matches: {len(b1_matches)}")
for m in b1_matches[:3]:
    print("--- MATCH ---")
    print(m[:300].strip())

# Book 2 sample
b2_idx = cairo.find('## 📘')
b3_idx = cairo.find('## 📙')
b2_text = cairo[b2_idx:b3_idx]
print("\n=== SAMPLE BOOK 2 EXERCISES ===")
b2_matches = re.findall(r'([0-9]+\s*[\-\.]\s*(?:أجب|اقرأ|تأمل|اِقرأ|كوّن|أدخل|حول|عين|اضبط|ضع|هات).*?)(?=\n[0-9]+\s*[\-\.]|\n####|\n---|\Z)', b2_text, re.DOTALL)
print(f"Book 2 pattern matches: {len(b2_matches)}")
for m in b2_matches[:3]:
    print("--- MATCH ---")
    print(m[:300].strip())
