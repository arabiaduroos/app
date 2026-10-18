import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

result = {}

for b in data['books']:
    b_num = b.get('book_num')
    b_title = b.get('title_ar')
    b_key = f"Book {b_num}: {b_title}"
    result[b_key] = []
    
    for u in b['units']:
        u_info = {
            'unit_id': u.get('id'),
            'title_ar': u.get('title_ar'),
            'topic_en': u.get('topic_en'),
            'topic_ur': u.get('topic_ur'),
            'total_questions': len(u.get('questions', [])),
            'tamreens': []
        }
        
        tam_dict = {}
        for q in u.get('questions', []):
            t_num = q.get('tamreen_num', 1)
            if t_num not in tam_dict:
                tam_dict[t_num] = {
                    'num': t_num,
                    'badge_ar': q.get('badge_ar', f'تَمْرِينٌ ({t_num})'),
                    'badge_ur': q.get('badge_ur', f'مشق ({t_num})'),
                    'badge_en': q.get('badge_en', f'Exercise ({t_num})'),
                    'count': 0,
                    'sample_ar': q.get('prompt_ar', '')[:50],
                    'sample_ur': q.get('prompt_ur', '')[:50]
                }
            tam_dict[t_num]['count'] += 1
            
        for t_num in sorted(tam_dict.keys()):
            u_info['tamreens'].append(tam_dict[t_num])
            
        result[b_key].append(u_info)

with open('scratch/tamreens_overview.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("Tamreens overview extracted successfully!")
