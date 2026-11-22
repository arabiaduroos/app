with open('transcriptions/Madinah-Book-1.html', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('اَلْحُرُوْفُ الْقَمَرَيَّةُ')
print(content[idx1:idx1+4000])
