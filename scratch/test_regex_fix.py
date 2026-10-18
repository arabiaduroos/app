import sys, re
sys.path.append('scratch')

sys.stdout.reconfigure(encoding='utf-8')

test_line = "(1) أجب عن الأسئلة الآتية:"
clean = re.sub(r'^[^\w\(\)\[\]]+', '', test_line).strip()
m = re.match(r'^(?:\(([0-9]+|[۱-۹]+)\)|([0-9]+|[۱-۹]+))\s*[\-\.]?\s*(.*)', clean)
if m:
    print("MATCHED:", m.group(1) or m.group(2), "->", m.group(3))
else:
    print("FAILED")
