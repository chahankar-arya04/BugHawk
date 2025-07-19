# 🐞 BugHawk – Lightweight Vulnerability Scanner (Flask Based)

BugHawk is a beginner-friendly web-based vulnerability scanner built using Python and Flask. It allows users to scan uploaded code snippets or text for known security issues and generate a basic report. Ideal for educational use or as a base for extending into more advanced tools.

## 🔍 Features

- Upload code/text input for scanning
- Detect basic security flaws using pattern-based analysis
- Assign severity levels
- Generate web-based reports
- Clean and simple UI (HTML + Bootstrap)

## 📁 Project Structure

BugHawk/
├── app/
│ ├── init.py # Flask app factory
│ ├── routes.py # Handles routing
│ ├── scanner.py # Vulnerability scanning logic
│ ├── utils.py # Helper functions
│ └── templates/
│ ├── index.html # Upload UI
│ └── report.html # Scan results
├── uploads/ # Uploaded input (if any)
├── reports/ # Scan output
├── run.py # Flask app runner
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

