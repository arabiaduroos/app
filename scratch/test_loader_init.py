import json, re, sys, os, random

sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)

# Load existing dataset
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Load Cairo transcription
with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo_md = f.read()

# Load Manifest
with open(r'C:\Users\Person\.gemini\antigravity\brain\871510d4-1766-4c62-b894-0270b402a9f3\madinah_curriculum_tamreens_manifest.md', 'r', encoding='utf-8') as f:
    manifest_md = f.read()

print("Loaded base datasets successfully.")
