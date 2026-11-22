with open('transcriptions/Madinah-Book-1.html', encoding='utf-8') as f:
    content = f.read()

target = 'id="b1_u3"'
idx = content.find(target)
print("Found at:", idx)
print(content[idx:idx+15000])
