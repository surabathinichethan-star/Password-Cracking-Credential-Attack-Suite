# Password Cracking & Credential Attack Suite
# Module: Brute Force Attack Simulator (Educational)

import hashlib
import itertools
import time

def generate_hash(password, algorithm):
    if algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported algorithm")

def brute_force(target_hash, algorithm, max_length=3):
    charset = "abcdefghijklmnopqrstuvwxyz0123456789"
    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            attempts += 1
            guess = ''.join(combo)

            if generate_hash(guess, algorithm) == target_hash:
                end_time = time.time()
                return guess, attempts, end_time - start_time

    return None, attempts, time.time() - start_time


if __name__ == "__main__":
    print("=== Brute Force Attack Simulator ===")

    target_hash = input("Enter target hash: ").strip()
    algorithm = input("Algorithm (md5/sha1/sha256): ").strip().lower()

    password, attempts, duration = brute_force(target_hash, algorithm)

    if password:
        print("\n[+] Password Cracked")
        print(f"Password : {password}")
        print(f"Attempts : {attempts}")
        print(f"Time     : {duration:.2f} seconds")
    else:
        print("\n[-] Password not cracked")
        print(f"Attempts : {attempts}")
        print(f"Time     : {duration:.2f} seconds")


