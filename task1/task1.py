def caesar(text, shift, mode):
    res = ""
    for c in text:
        if c.isupper():
            if mode == "e":
                res += chr((ord(c) - 65 + shift) % 26 + 65)
            else:
                res += chr((ord(c) - 65 - shift) % 26 + 65)
        elif c.islower():
            if mode == "e":
                res += chr((ord(c) - 97 + shift) % 26 + 97)
            else:
                res += chr((ord(c) - 97 - shift) % 26 + 97)
        else:
            res += c
    return res

print("1 Encrypt")
print("2 Decrypt")
ch = input("Enter choice: ")
msg = input("Enter message: ")
s = int(input("Enter shift: "))

if ch == "1":
    print("Encrypted:", caesar(msg, s, "e"))
elif ch == "2":
    print("Decrypted:", caesar(msg, s, "d"))
else:
    print("Invalid choice")

