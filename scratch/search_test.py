import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob('transcriptions/*.*') + glob.glob('data/*.*'):
    content = open(f, encoding='utf-8').read()
    if 'مرضت' in content or 'حججت' in content:
        print(f"Found in {f}")
        for l in content.splitlines():
            if 'حججت' in l:
                print(f"  {l[:100]}")
