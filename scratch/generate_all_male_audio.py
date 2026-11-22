import asyncio
import edge_tts
import hashlib
import json
import os
import re

# Load app.js to get all data
with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('let DATA = ')
end = text.find(';\n', start)
data = json.loads(text[start+len('let DATA = '):end])

# Function to clean text exactly as in app.js
def clean_arabic(txt):
    if not txt:
        return ''
    t = re.sub(r'\[.*?\]', '', txt)
    t = re.sub(r'[\(（][۰-۹0-9]+[\)）]', '', t)
    t = re.sub(r'[•|⬅️➡️➔⬇️💡✨⭐\?؟\.,!:]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

all_phrases = set()

# Collect from cards
for b in data['books']:
    for u in b.get('units', []):
        for c in u.get('cards', []):
            ar = c.get('arabic', '')
            if '➔' in ar or '->' in ar or '•' in ar:
                for part in re.split(r'[➔\->•]', ar):
                    cl = clean_arabic(part)
                    if cl:
                        all_phrases.add(cl)
            cl = clean_arabic(ar)
            if cl:
                all_phrases.add(cl)
            if 'words' in c and isinstance(c['words'], list):
                for w in c['words']:
                    wcl = clean_arabic(w.get('ar', ''))
                    if wcl:
                        all_phrases.add(wcl)

# Moon & Sun items
moon_words = ['اَلْأَبُ', 'اَلْبَابُ', 'اَلْجَنَّةُ', 'اَلْحِمَارُ', 'اَلْخُبْزُ', 'اَلْعَيْنُ', 'اَلْغَدَاءُ', 'اَلْفَمُ', 'اَلْقَمَرُ', 'اَلْكَلْبُ', 'اَلْمَاءُ', 'اَلْوَلَدُ', 'اَلْهَوَاءُ', 'اَلْيَدُ']
sun_words = ['التَّاجِرُ', 'الثَّوْبُ', 'الدِّيكُ', 'الذَّهَبُ', 'الرَّجُلُ', 'الزَّهْرَةُ', 'السَّمَكُ', 'الشَّمْسُ', 'الصَّدْرُ', 'الضَّيْفُ', 'الطَّالِبُ', 'الظَّهْرُ', 'اللَّحْمُ', 'النَّجْمُ']
vocab_words = ['الْقَمَرُ', 'جَدِيدٌ', 'قَدِيمٌ', 'وَسِخٌ', 'نَظِيفٌ', 'حَارٌّ', 'بَارِدٌ', 'صَغِيرٌ', 'كَبِيرٌ', 'مَفْتُوحٌ', 'مَكْسُورٌ', 'ثَقِيلٌ', 'خَفِيفٌ', 'جَمِيلٌ', 'وَاقِفٌ', 'جَالِسٌ', 'حُلْوٌ', 'مَرِيضٌ', 'الدُّكَّانُ', 'غَنِيٌّ', 'طَوِيلٌ', 'فَقِيرٌ', 'قَصِيرٌ', 'التُّفَّاحُ', 'إِمَامٌ', 'حَجَرٌ', 'سُكَّرٌ', 'لَبَنٌ']

for w in moon_words + sun_words + vocab_words:
    cl = clean_arabic(w)
    if cl:
        all_phrases.add(cl)

print(f"Total unique Arabic phrases to synthesize: {len(all_phrases)}")

os.makedirs('audio', exist_ok=True)

def get_hash(txt):
    return hashlib.md5(txt.encode('utf-8')).hexdigest()[:10]

audio_map = {}

async def generate_phrase(phrase, sem):
    h = get_hash(phrase)
    filename = f"aud_{h}.mp3"
    filepath = os.path.join('audio', filename)
    audio_map[phrase] = f"audio/{filename}"

    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        return

    async with sem:
        try:
            communicate = edge_tts.Communicate(phrase, 'ar-SA-HamedNeural')
            await communicate.save(filepath)
        except Exception as e:
            print(f"Error on {phrase}: {e}")

async def main():
    sem = asyncio.Semaphore(6)
    tasks = [generate_phrase(p, sem) for p in all_phrases]
    await asyncio.gather(*tasks)
    print(f"Synthesized all audio files successfully!")

    with open('audio_index.json', 'w', encoding='utf-8') as f:
        json.dump(audio_map, f, ensure_ascii=False, indent=2)
    print("Saved audio_index.json")

asyncio.run(main())
