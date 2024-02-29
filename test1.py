import rail_fence_cipher

text = "CRYPTOLOGY IS THE PRACTICE AND STUDY OF TECHNIQUES FOR SECURE COMMUNICATION IN THE PRESENCE OF THIRD PARTIES CALLED ADVERSARIES."
key = (4, 5)

print("Test 1:")
print("Input message=", text)
print("Key=", key)
print("Encrypted message=", rail_fence_cipher.rail_fence_encrypt(text, key))
