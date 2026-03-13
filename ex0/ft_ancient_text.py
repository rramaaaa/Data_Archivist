#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()

    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        file = open("ancient_fragment.txt", "r")
        print("Connection established...")
        print()

        print("RECOVERED DATA:")
        data = file.read()
        print(data)
        file.close()
        print()

        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
