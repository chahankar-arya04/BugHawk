from flask import Blueprint, render_template, request
import os
from .scanner import scan_file  # ✅ Make sure this import works

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/scan', methods=['POST'])
def scan():
    file = request.files.get('logfile')
    if not file:
        return "No file uploaded.", 400

    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    # 🔁 Replace the simple string with scanner findings
    findings = scan_file(filepath)
    result = f"Scan completed for {file.filename}:\n" + '\n'.join(findings)

    return render_template('report.html', result=result)
