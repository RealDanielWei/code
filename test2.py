import rail_fence_cipher

text = 'TAOTINEN KAT I ODIOAEI OHHLSCTE TTETOEL BI IHI GAO   EPSEA TO SS  EEK  ELRCPTSIY EANRPHMCYEK E CREAAIEJURTE  IEASHI MA DRN RH  AUWTA RF EFTFHENTPSF Q   TAILB E TTECAPMSIYIY SRPURNTBL YCL OANAO  E  TVREAOSHOTTNULSRHK'
key = (3, 3)

print("Test 2:")
print("Input message=", text)
print("Key=", key)
print("Decrypted message=", rail_fence_cipher.rail_fence_decrypt(text, key))
