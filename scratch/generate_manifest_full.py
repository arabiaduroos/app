import sys, os, json, re

sys.stdout.reconfigure(encoding='utf-8')

# Let's write the generator script that compiles the complete manifest
# and outputs the exact table with columns:
# lesson | page_number | tamreen_or_snippet | description | question_count

manifest_path = r"C:\Users\Person\.gemini\antigravity\brain\871510d4-1766-4c62-b894-0270b402a9f3\madinah_curriculum_tamreens_manifest.md"

# Let's inspect the existing manifest or overwrite with the comprehensive verified version
print("Building master generator...")
