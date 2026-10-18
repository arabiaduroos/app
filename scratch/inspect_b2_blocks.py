import json, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('data/madinah_books.json', encoding='utf-8'))
for b_idx, u_id, blk_idx in [(2, 'b2_u1', 20), (2, 'b2_u29', 21), (1, 'b1_u4', 7)]:
    u = [u for b in d['books'] for u in b['units'] if u['id'] == u_id][0]
    blk = u['blocks'][blk_idx]
    print(f"\n=== {u_id} Block {blk_idx} ===")
    for i, w in enumerate(blk.get('words', [])):
        print(f"  [{i}] {w.get('ar')} | {w.get('ur')}")
