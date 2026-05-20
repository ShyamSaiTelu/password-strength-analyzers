
import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?":{}|<>]", password):
        strength += 1

    if strength <= 2:
        remarks = "Weak Password"
    elif strength == 3:
        remarks = "Moderate Password"
    else:
        remarks = "Strong Password"

    return strength, remarks

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength, remarks = check_password_strength(pwd)
    print(f"Password Strength Score: {strength}/5")
    print(f"Assessment: {remarks}")
