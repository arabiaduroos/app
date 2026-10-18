import json, os

with open('scratch/tamreens_overview.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

artifact_dir = r"C:\Users\Person\.gemini\antigravity\brain\871510d4-1766-4c62-b894-0270b402a9f3"
output_path = os.path.join(artifact_dir, "madinah_curriculum_tamreens_manifest.md")

lines = []
lines.append("# 📚 Master Curriculum: All Tamreens Across All 71 Chapters")
lines.append("> **Madinah Arabic Series (Books 1, 2, and 3) by Dr. V. Abdur Rahim**")
lines.append("> Comprehensive verification manifest of all exercises and learning units.\n")

lines.append("## 📊 Overall Summary Statistics")
lines.append("| Book | Units / Chapters | Total Exercises (Tamreens) | Total Interactive Questions | Key Focus Areas |")
lines.append("| :--- | :---: | :---: | :---: | :--- |")
lines.append("| **Book 1 (الْجُزْءُ الْأَوَّلُ)** | 23 | 59 Tamreens | 208 Questions | Demonstratives, Idafah, Prepositions, Attached Pronouns, Sound Plurals, Colors, Diptotes |")
lines.append("| **Book 2 (الْجُزْءُ الثَّانِي)** | 31 | 114 Tamreens | 152 Questions | Inna & Sisters, Past & Present Verbs, Kaana, Moods (Marfoo/Mansub/Majzoom), Irregular Verbs |")
lines.append("| **Book 3 (الْجُزْءُ الثَّالِثُ)** | 17 | 68 Tamreens | 255 Questions | Advanced Syntax, Dropping Nun in Idafah (Unit 9: 14 tamreens), Conditionals, Derived Verb Forms II-X |")
lines.append("| **GRAND TOTAL** | **71 Units** | **241 Tamreens** | **615 Questions** | **Complete authentic curriculum with Tashkeel and dual Urdu/English support** |\n")

lines.append("---\n")

for book_name, units in d.items():
    book_badge = "📗" if "Book 1" in book_name else ("📘" if "Book 2" in book_name else "📙")
    lines.append(f"## {book_badge} {book_name}")
    lines.append(f"**Total Chapters**: {len(units)} Units\n")
    
    for u in units:
        lines.append(f"### {u['unit_id'].upper()}: {u['title_ar']} — {u['topic_en']}")
        lines.append(f"- **Topic (Urdu)**: {u.get('topic_ur', '')}")
        lines.append(f"- **Total Questions**: {u['total_questions']} Questions")
        lines.append(f"- **Tamreens Breakdown**:")
        lines.append("| Tamreen # | Arabic Title / Badge | Urdu Description | English Description | Questions Count |")
        lines.append("| :---: | :--- | :--- | :--- | :---: |")
        
        for t in u['tamreens']:
            lines.append(f"| **{t['num']}** | {t['badge_ar']} | {t['badge_ur']} | {t['badge_en']} | {t['count']} |")
        lines.append("\n")

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Artifact written to {output_path}")
print(f"Total lines: {len(lines)}")
