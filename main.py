
# KONAMI TYPOSQUATTING LAB
# Educational cybersecurity demonstration

legitimate = "konami.com"
suspicious = "konamii.com"

print("================================")
print("     KONAMI SECURITY LAB")
print("================================")

print("Legitimate domain:", legitimate)
print("Look-alike domain:", suspicious)

if legitimate == suspicious:
    print("Domains match.")
else:
    print("\nWARNING: DOMAIN MISMATCH!")
    print("The two website addresses are different.")
    print("Check carefully before visiting.")
