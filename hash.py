import hashlib

string=1224
string = str(string)
encoded=string.encode()
result = hashlib.sha256(encoded)
print("String : %s"%string, end ="")
print("\nHexadecimal equivalent: ",result.hexdigest())