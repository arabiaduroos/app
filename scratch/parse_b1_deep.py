import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b1_text = text[b1_idx:b2_idx]

# Split by "### "
sections = re.split(r'\n###\s+', b1_text)

print(f"Total units in Book 1: {len(sections)-1}")

B1_PAGES = {
    1: 5, 2: 12, 3: 14, 4: 21, 5: 27, 6: 33, 7: 39, 8: 42, 9: 47,
    10: 54, 11: 61, 12: 63, 13: 68, 14: 82, 15: 87, 16: 92, 17: 96,
    18: 100, 19: 105, 20: 109, 21: 114, 22: 117, 23: 120
}

for idx, s in enumerate(sections[1:], 1):
    lines = [l.strip() for l in s.split('\n') if l.strip()]
    header = lines[0]
    p_start = B1_PAGES.get(idx, 0)
    p_end = B1_PAGES.get(idx+1, 124) - 1 if idx < 23 else 123
    print(f"\n=======================================================")
    print(f"Lesson {idx}: {header} (pp. {p_start}-{p_end})")
    print(f"=======================================================")
    
    # We want to identify each tamreen and snippet
    # In Cairo.md, exercises are denoted by:
    # "#### ✍️ تمرين (X)" or "#### ✍️ تـمـــــارين" or "- (X) ..." or "- اقرأ ..." or snippets
    for l in lines:
        if l.startswith('#### ✍️') or l.startswith('#### 🗂️') or re.match(r'^-\s*\(?[0-9]+\)?\s*(أجب|أضف|اقرأ|اِقْرَأْ|كوّن|كون|صَحِّحْ|صحح|تأمل|اختر|املأ|اِمْلَأْ|هات|صل|ضع|عين|أدخل|حول)', l):
            print("  ", l[:75])
        elif any(k in l for k in ['محمدٌ : يا محمدُ', 'اِسمٌ :', 'اِبْنٌ :', 'الحروف القمرية والحروف الشمسية', 'الممنوع من الصرف']):
            print("   [SNIPPET]", l[:75])
