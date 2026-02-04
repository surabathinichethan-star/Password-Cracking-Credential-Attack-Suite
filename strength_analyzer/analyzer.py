# Password Cracking & Credential Attack Suite
# Module: Password Strength Analyzer (Defensive)

import math
import re

def calculate_entropy(password):
    charset_size = 0
    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"[0-9]", password):
        charset_size += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset_size += 32

    if charset_size == 0:
        return 0

    return round(len(password) * math.log2(charset_size), 2)


def analyze_password(password):
    issues = []

    if len(password) < 8:
        issues.append("Too short (min 8 characters)")

    if not re.search(r"[A-Z]", password):
        issues.append("No uppercase letters")

    if not re.search(r"[a-z]", password):
        issues.append("No lowercase letters")

    if not re.search(r"[0-9]", password):
        issues.append("No numbers")

    if not re.search(r"[^a-zA-Z0-9]", password):
        issues.append("No special characters")

    entropy = calculate_entropy(password)

    if entropy < 40:
        risk = "CRITICAL"
    elif entropy < 60:
        risk = "WEAK"
    elif entropy < 80:
        risk = "MEDIUM"
    else:
        risk = "STRONG"

    return entropy, risk, issues


if __name__ == "__main__":
    print("=== Password Strength Analyzer ===")

    pwd = input("Enter password to analyze: ")
    entropy, risk, issues = analyze_password(pwd)

    print(f"\nEntropy Score: {entropy}")
    print(f"Risk Level  : {risk}")

    if issues:
        print("\nIssues Found:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("\nPassword meets all complexity requirements.")
