import re

def scan_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    findings = []

    if 'eval(' in content:
        findings.append("⚠️ Uses eval(), which can be dangerous.")
    if 'os.system' in content:
        findings.append("⚠️ Uses os.system(), possible command injection.")
    if 'input(' in content:
        findings.append("⚠️ Uses input(), might be collecting sensitive data.")
    if 'subprocess' in content:
        findings.append("⚠️ Uses subprocess, check for command execution risks.")

    return findings if findings else ["✅ No known vulnerabilities found."]
