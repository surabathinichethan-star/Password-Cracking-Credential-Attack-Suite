# Password Cracking & Credential Attack Suite

## 📌 Project Overview
The Password Cracking & Credential Attack Suite is a Python-based security auditing framework designed to simulate real-world password attacks in a **controlled and ethical environment**.

The project helps understand how weak passwords are exploited and how organizations can strengthen authentication security.

This project follows both **Red Team (attack simulation)** and **Blue Team (defensive analysis)** perspectives.

---

## 🎯 Project Objectives
- Generate custom password dictionaries
- Simulate password hashing mechanisms
- Perform controlled brute-force attack simulations
- Analyze password strength using entropy and complexity
- Generate professional security audit reports
- Recommend secure password policies

---

## 🧰 Tools & Technologies
- **Programming Language:** Python
- **Libraries Used:** hashlib, itertools, math, re, datetime
- **Platform:** Windows
- **Version Control:** Git & GitHub

---

## 🗂️ Project Structure

Password-Cracking-Credential-Attack-Suite/

├── dictionary_generator/

│ └── generator.py

├── hashing/

│ └── hash_generator.py

├── brute_force/

│ └── brute_force.py

├── strength_analyzer/

│ └── analyzer.py

├── reports/

│ ├── report_generator.py

│ └── audit_report.txt

├── data/

│ └── wordlist.txt

└── README.md


---

## ⚙️ Modules Description

### 1️⃣ Dictionary Generator
- Generates custom wordlists based on user input
- Applies mutation rules (uppercase, numbers, symbols, leetspeak)
- Simulates real-world password profiling

### 2️⃣ Hash Generator
- Converts plaintext passwords into cryptographic hashes
- Supports MD5, SHA1, SHA256, SHA512
- Demonstrates how passwords are stored securely

### 3️⃣ Brute-Force Attack Simulator
- Performs controlled brute-force simulations
- Uses hashes instead of plaintext passwords
- Calculates number of attempts and time-to-crack

### 4️⃣ Password Strength Analyzer
- Evaluates password complexity and entropy
- Assigns risk levels (CRITICAL, WEAK, MEDIUM, STRONG)
- Identifies weaknesses and missing security controls

### 5️⃣ Audit Report Generator
- Generates a professional security audit report
- Includes findings, risk assessment, and remediation steps
- Mimics real SOC / security audit documentation

---

## ▶️ How to Run the Project

### Step 1: Generate Dictionary
```powershell
cd dictionary_generator
python generator.py

Step 2: Generate Hashes
cd hashing
python hash_generator.py

Step 3: Brute-Force Simulation
cd brute_force
python brute_force.py

Step 4: Analyze Password Strength
cd strength_analyzer
python analyzer.py

Step 5: Generate Audit Report
cd reports
python report_generator.py

📄 Sample Outputs

Generated wordlist (wordlist.txt)

Password cracking results with time-to-crack

Password entropy and risk analysis

Security audit report (audit_report.txt)

🔐 Ethical Disclaimer

This project is strictly for educational and ethical security testing purposes only.
All simulations are performed on self-created test data.
Unauthorized use of these techniques on real systems is illegal.

📈 Learning Outcomes

Understanding of password storage and hashing

Practical exposure to credential attack techniques

Ability to audit password security

Experience with Red Team and Blue Team methodologies

Hands-on Python and GitHub workflow

👤 Author

Chethan Surabathini
Cybersecurity Intern | SOC Analyst Aspirant
