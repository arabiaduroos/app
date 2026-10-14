import re

css = open('styles.css', encoding='utf-8').read()

classes_in_css = set(re.findall(r'\.([a-zA-Z0-9_\-]+)', css))

html = open('index.html', encoding='utf-8').read()
html_classes = set()
for m in re.findall(r'class=["\']([^"\']+)["\']', html):
    for c in m.split():
        html_classes.add(c)

missing_classes = html_classes - classes_in_css
print("Total CSS classes:", len(classes_in_css))
print("Total HTML classes:", len(html_classes))
print("Missing classes in CSS:", missing_classes)
