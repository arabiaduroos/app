import fitz
from PIL import Image
import os

# Let's inspect pages in Book 2 to find lesson start pages
# In Book 2, a lesson start page typically has a line "( X ) الدرس ..." or "الدرس ..."
# Let's write a python script that saves crops around likely positions, or let's search
# In Madinah Book 2, let's look at the dialogue text of each lesson in Madinah-Book-2.html

import re

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    b2_html = f.read()

lessons_b2 = re.findall(r'<h2 class="unit-title">([\s\S]*?)</h2>', b2_html)
print(f"Book 2 lessons in HTML: {len(lessons_b2)}")

with open('transcriptions/Madinah-Book-3.html', 'r', encoding='utf-8') as f:
    b3_html = f.read()

lessons_b3 = re.findall(r'<h2 class="unit-title">([\s\S]*?)</h2>', b3_html)
print(f"Book 3 lessons in HTML: {len(lessons_b3)}")
