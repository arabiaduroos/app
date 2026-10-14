import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")

data = json.load(open("data/madinah_books.json", encoding="utf-8"))

total_blocks = 0
issues = []

for b_idx, book in enumerate(data.get("books", [])):
    book_num = book.get("book_num", b_idx + 1)
    for unit in book.get("units", []):
        u_num = unit.get("unit_num")
        for blk_idx, b in enumerate(unit.get("blocks", [])):
            sec = b.get("section", "lesson")
            bt = b.get("type", "")
            raw_text = (b.get("text") or "").strip()
            
            # Skip exercises or header markers
            if sec == "exercises" or bt == "exercise_line":
                continue
            if re.match(r"^(تمارين|تمرين|التدريبات|اقرأ واكتب)", raw_text):
                continue
            if bt in ["vocab_table", "grammar_pairs"]:
                continue
            if not raw_text or re.match(r"^[=\-•\s\(\)]+$", raw_text):
                continue

            total_blocks += 1
            raw_en = (b.get("en") or "").strip()
            raw_ur = (b.get("ur") or "").strip()

            # Check if EN has no latin letters
            has_latin_en = bool(re.search(r"[a-zA-Z]", raw_en))
            is_en_same_as_ar = raw_en and (raw_en == raw_text or re.sub(r"\s+", "", raw_en) == re.sub(r"\s+", "", raw_text))
            is_ur_same_as_ar = raw_ur and (raw_ur == raw_text or re.sub(r"\s+", "", raw_ur) == re.sub(r"\s+", "", raw_text))

            if is_en_same_as_ar:
                issues.append(f"Book {book_num} Unit {u_num} Blk {blk_idx}: EN is identical to Arabic!")
            elif not has_latin_en and raw_en:
                issues.append(f"Book {book_num} Unit {u_num} Blk {blk_idx}: EN has no English letters ('{raw_en[:30]}')")
            elif not raw_en:
                issues.append(f"Book {book_num} Unit {u_num} Blk {blk_idx}: EN is missing! AR: '{raw_text[:30]}'")

            if is_ur_same_as_ar:
                issues.append(f"Book {book_num} Unit {u_num} Blk {blk_idx}: UR is identical to Arabic!")
            elif not raw_ur:
                issues.append(f"Book {book_num} Unit {u_num} Blk {blk_idx}: UR is missing! AR: '{raw_text[:30]}'")

print(f"Total lesson blocks analyzed across all 3 books: {total_blocks}")
print(f"Total issues found: {len(issues)}")
if issues:
    for iss in issues[:20]:
        print("  -", iss)
    if len(issues) > 20:
        print(f"  ... and {len(issues) - 20} more.")
else:
    print("PERFECT! 100% of lesson blocks have valid, distinct English and Urdu translations.")
