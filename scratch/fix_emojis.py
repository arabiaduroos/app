import os

path = r"C:\Users\Person\.gemini\antigravity\brain\548db058-a481-48f4-9024-0b3a7fd2647c\scratch\render_split_pages.py"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Replace missing emojis
c = c.replace('"🫏"', '"🐴"')
c = c.replace('"🪙"', '"💰"')
c = c.replace('"🫁"', '"🛡️"')
c = c.replace('"🧳"', '"🤝"')

# Make sure al-prefix is styled
c = c.replace(
    '<span class="word-ar kufi-font">{word}</span>',
    '<span class="word-ar kufi-font">{word_formatted}</span>'
)

# And in the loop:
old_loop = """    for idx, (letter, word, en, ur, em) in enumerate(items, 1):
        rows_html += f\"\"\""""

new_loop = """    for idx, (letter, word, en, ur, em) in enumerate(items, 1):
        if is_qamari:
            word_formatted = f'<span style="color:#1d4ed8; font-weight:800;">اَلْـ</span><span style="color:#0f172a;">{word.replace("اَلْـ", "")}</span>'
        else:
            word_formatted = f'<span style="color:#b45309; font-weight:800;">الـ</span><span style="color:#0f172a;">{word.replace("الـ", "")}</span>'
        rows_html += f\"\"\""""

c = c.replace(old_loop, new_loop)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated render_split_pages.py successfully!")
