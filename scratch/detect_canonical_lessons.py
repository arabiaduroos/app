import sys, re

sys.stdout.reconfigure(encoding='utf-8')

for b_num, fname in [(1, 'transcriptions/Madinah-Book-1.html'), 
                     (2, 'transcriptions/Madinah-Book-2.html'), 
                     (3, 'transcriptions/Madinah-Book-3.html')]:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # find all lesson mentions
    raw_lessons = re.findall(r'<div class="txt-line"><div>([^<]*?الْدَّرْسُ[^<]*?|[^<]*?الدَّرْسُ[^<]*?|[^<]*?الدرس[^<]*?)</div><div class="ur">([^<]*?)</div></div>', html)
    print(f"\n=================== BOOK {b_num} ===================")
    print(f"Total raw lesson lines: {len(raw_lessons)}")
    unique_lessons = []
    seen = set()
    for ar, ur in raw_lessons:
        # filter out lines that just mention lesson inside dialogue e.g. "في الدرس" or "بعد الدرس"
        clean = re.sub(r'[🔹📖🏫👨‍🎓\*]', '', ar).strip()
        if re.search(r'^(الْدَّرْسُ|الدَّرْسُ|الدرس)\s+(الأَوَّل|الْأَوَّل|الأول|الثاني|الثَّانِي|الثالث|الثَّالِث|الرابع|الرَّابِع|الخامس|الْخَامِس|السادس|السَّادِس|السابع|السَّابِع|الثامن|الثَّامِن|التاسع|التَّاسِع|العاشر|الْعَاشِر|الحادي|الْحَادِي|الثاني عشر|الثَّانِيَ عَشَرَ|الثالث عشر|الرابع عشر|الخامس عشر|السادس عشر|السابع عشر|الثامن عشر|التاسع عشر|العشرون|الْعِشْرُونَ|الحادي والعشرون|الثاني والعشرون|الثالث والعشرون|الرابع والعشرون|الخامس والعشرون|السادس والعشرون|السابع والعشرون|الثامن والعشرون|التاسع والعشرون|الثلاثون|الحادي والثلاثون)', clean):
            if clean not in seen:
                seen.add(clean)
                unique_lessons.append((clean, ur.strip()))
    print(f"Unique canonical lessons detected: {len(unique_lessons)}")
    for l_ar, l_ur in unique_lessons:
        print(f"  {l_ar}  |  {l_ur}")
