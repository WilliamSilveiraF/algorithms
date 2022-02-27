times = input()
hexSequence = input().replace(" ", "")
print(bytearray.fromhex(hexSequence).decode())
