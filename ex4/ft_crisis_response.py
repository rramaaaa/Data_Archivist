#!/usr/bin/env python3


def access_archive(name: str) -> None:
    try:
        if name == "standard_archive.txt":
            print(
                "ROUTINE ACCESS: Attempting access to 'standard_archive.txt'.."
            )
        else:
            print(f"CRISIS ALERT: Attempting access to '{name}'...")

        with open(name, "r") as file:
            data = file.read()
            print(f"SUCCESS: Archive recovered - \"{data}\"")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    access_archive("lost_archive.txt")
    print()

    access_archive("classified_vault.txt")
    print()

    access_archive("standard_archive.txt")
    print()

    print("All crisis scenarios handled successfully. Archives secure.")
