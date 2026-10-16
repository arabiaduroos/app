import os, subprocess

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
out_path = os.path.abspath(r'scratch\screenshot_mobile_home.png')

cmd = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=390,844',
    f'--screenshot={out_path}',
    'http://localhost:8080/index.html'
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("Output file exists:", os.path.exists(out_path))
