import re

html = open('index.html', encoding='utf-8').read()
js = open('app.js', encoding='utf-8').read()

html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', html))
js_ids = set(re.findall(r'getElementById\(["\']([^"\']+)["\']\)', js))

missing = js_ids - html_ids
print('Total HTML IDs count:', len(html_ids))
print('Total JS getElementById count:', len(js_ids))
print('Missing IDs in HTML:', missing)

assert len(missing) == 0, f"Found missing IDs: {missing}"
print("SUCCESS: 100% ID Match between HTML and app.js!")
