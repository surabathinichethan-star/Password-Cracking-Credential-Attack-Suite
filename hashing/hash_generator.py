# Password Cracking & Credential Attack Suite
# Module: Hash Generator

import hashlib

def generate_hashes(password):
    hashes = {
        "MD5": hashlib.md5(password.encode()).hexdigest(),
        "SHA1": hashlib.sha1(password.encode()).hexdigest(),
        "SHA256": hashlib.sha256(password.encode()).hexdigest(),
        "SHA512": hashlib.sha512(password.encode()).hexdigest()
    }
    return hashes


if __name__ == "__main__":
    print("=== Password Hash Generator ===")
    password = input("Enter password to hash: ")

    result = generate_hashes(password)

    print("\nGenerated Hashes:")
    for algo, value in result.items():
        print(f"{algo}: {value}")
