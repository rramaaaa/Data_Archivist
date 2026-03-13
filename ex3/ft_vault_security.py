#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()

    print("SECURE EXTRACTION:")
    with open("classified_data.txt", "r") as file:
        data = file.read()
        print(data)
    print()

    print("SECURE PRESERVATION:")
    with open("security_archived", "w") as file:
        file.write("[CLASSIFIED] New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")
    print()

    print("All vault operations completed with maximum security.")
