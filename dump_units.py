import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch_b2_texts.json', encoding='utf-8') as f:
    texts = json.load(f)

def dump_units(start_u, end_u):
    for u in range(start_u, end_u + 1):
        items = [x for x in texts if x['unit'] == u]
        print(f"\n==================== UNIT {u} ({len(items)} items) ====================")
        for i, it in enumerate(items):
            spk = f"[{it['speaker']}] " if it.get('speaker') else ""
            print(f"{i+1:2d}. ({it['type']}) {spk}{it['ar']}")

if __name__ == '__main__':
    u_start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    u_end = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    dump_units(u_start, u_end)
