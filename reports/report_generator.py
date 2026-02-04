from datetime import datetime

def generate_report(password, hash_algo, cracked, entropy, risk):
    with open("audit_report.txt", "w") as report:
        report.write("PASSWORD SECURITY AUDIT REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(f"Audit Date       : {datetime.now()}\n")
        report.write(f"Hash Algorithm   : {hash_algo}\n")
        report.write(f"Password Cracked : {'YES' if cracked else 'NO'}\n")
        report.write(f"Entropy Score    : {entropy}\n")
        report.write(f"Risk Level       : {risk}\n\n")

        report.write("Findings:\n")
        if cracked:
            report.write("- Password was cracked using brute-force simulation.\n")
        else:
            report.write("- Password resisted brute-force simulation.\n")

        report.write("\nRecommendations:\n")
        report.write("- Enforce minimum length of 12 characters\n")
        report.write("- Require uppercase, lowercase, numbers, and symbols\n")
        report.write("- Prevent reuse of common or breached passwords\n")
        report.write("- Implement account lockout and rate limiting\n")

    print("[+] Audit report generated: audit_report.txt")


if __name__ == "__main__":
    generate_report(
        password="abc",
        hash_algo="MD5",
        cracked=True,
        entropy=14.1,
        risk="CRITICAL"
    )
