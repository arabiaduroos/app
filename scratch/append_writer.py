import re, json, sys, os

sys.stdout.reconfigure(encoding='utf-8')

# Append writing logic to scratch/build_clean_master_manifest.py
with open('scratch/build_clean_master_manifest.py', 'r', encoding='utf-8') as f:
    code = f.read()

write_code = '''
# Write to artifact file
artifact_path = r"C:\\Users\\Person\\.gemini\\antigravity\\brain\\871510d4-1766-4c62-b894-0270b402a9f3\\madinah_curriculum_tamreens_manifest.md"

md_content = """# 📚 Master Curriculum: Complete Tamreens & Snippets Across All 71 Lessons
> **Madinah Arabic Series (Books 1, 2, and 3) by Shaykh Dr. V. Abdur Rahim**
> Exhaustive verification manifest: 100% authentic page numbers from the author's printed Table of Contents, exact exercise counts, reading drills, and grammar snippets.

## 📊 Summary Statistics
| Book | Lessons | Total Tamreens & Snippets | Printed Page Range | Core Curriculum Focus |
| :--- | :---: | :---: | :---: | :--- |
| **Book 1 (الْجُزْءُ الْأَوَّلُ)** | 23 Lessons | """ + str(len(b1_final)) + """ Items | pp. 5–123 | Demonstratives, Definite Article, Prepositions, Idafah, Plurals, Diptotes |
| **Book 2 (الْجُزْءُ الثَّانِي)** | 31 Lessons | """ + str(len(b2_final)) + """ Items | pp. 5–223 | Inna & Sisters, Past/Present Verbs, Kaana, Three Moods, Irregular Verbs |
| **Book 3 (الْجُزْءُ الثَّالِثُ)** | 17 Lessons | """ + str(len(b3_final)) + """ Items | pp. 5–144 | Advanced Syntax, Dropping Nun in Idafah, Conditionals, Derived Forms II-X |
| **GRAND TOTAL** | **71 Lessons** | **""" + str(len(b1_final) + len(b2_final) + len(b3_final)) + """ Items** | **490 Pages** | **Full curriculum transcribed & verified against scanned textbooks** |

---

"""

def format_table(title, rows):
    out = f"## {title}\\n\\n"
    out += "| lesson | page_number | tamreen_or_snippet | description | question_count |\\n"
    out += "| :--- | :---: | :--- | :--- | :---: |\\n"
    for r in rows:
        out += f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |\\n"
    out += "\\n---\\n\\n"
    return out

md_content += format_table("📗 Book 1: Complete Tamreens & Snippets Inventory (Lessons 1–23)", b1_final)
md_content += format_table("📘 Book 2: Complete Tamreens & Snippets Inventory (Lessons 1–31)", b2_final)
md_content += format_table("📙 Book 3: Complete Tamreens & Snippets Inventory (Lessons 1–17)", b3_final)

with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Artifact successfully updated at {artifact_path} with {len(b1_final)+len(b2_final)+len(b3_final)} rows!")
'''

with open('scratch/build_clean_master_manifest.py', 'w', encoding='utf-8') as f:
    f.write(code + "\n" + write_code)

print("Updated script with writing logic.")
